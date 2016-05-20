from gpiozero import MotionSensor
from picamera import PiCamera

camera = PiCamera()
pir = MotionSensor(4)
while True:
    if motion_detected:
	    camera.start_preview()
	else:
	    camera.stop_preview()
