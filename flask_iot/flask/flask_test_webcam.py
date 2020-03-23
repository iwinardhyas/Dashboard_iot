from flask import Flask, render_template, Response, g
# import picamera
import cv2
import socket
import io
import numpy as np
import datetime
import time
import sys
from gy_302_BH1750 import sensor_gy
from openweather import data_openweather
from dht_11 import data_dht

app = Flask(__name__)

# global time
# time = datetime.datetime.now()


@app.route('/')
def index():
   # return "Hello Worldsdfdsdfsdf!"
#     """Video streaming"""
    # data_light = sensor_gy()
    hum_room,temp_room = data_dht()
    temp,hum,press,weat,wind = data_openweather()
    data_light = 10

    return render_template('index.html',data_light=data_light,temp=temp,
        hum=hum,press=press,weat=weat,wind=wind,hum_room=hum_room,temp_room=temp_room)

def gen():
    """Video streaming generator function."""
    vc = cv2.VideoCapture("rtsp://admin:admin@192.168.18.46:554/mode=real&idc=1&ids=1")

    while True:
        rval, frame = vc.read()
        date_ = datetime.datetime.now()
        frame = cv2.resize(frame,(640,480))
        cv2.imwrite('t.jpg', frame)
        yield (b'--frame\r\n'
                b'Content-Type: image/jpeg\r\n\r\n' + open('t.jpg', 'rb').read() + b'\r\n')

@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    date = gen()
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
   # app.run(host='192.168.18.118', debug=True, threaded=True)
   app.run(host='0.0.0.0', debug=True, threaded=True)
