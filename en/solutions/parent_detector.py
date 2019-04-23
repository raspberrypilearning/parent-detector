from gpiozero import MotionSensor
from picamera import Picamera
from datetime import datetime

pir = MotionSensor(4)
camera = PiCamera()

while True:
    filename = "{0:%Y}-{0:%m}-{0:%d}".format(now)
    pir.wait_for_motion()
    camera.start_recording(filename)
    pir.wait_for_no_motion()
    camera.stop_recording()
