## Set up the camera preview

--- task ---
At the start of your program, import the `Camera` class from the `picamzero` library so that you can use it to control the Camera Module.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1 
line_highlights: 2
---
from gpiozero import MotionSensor
from picamzero import Camera
--- /code ---

--- /task ---

--- task ---
Now, create a `Camera` object. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 1 
line_highlights: 5
---
from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
cam = Camera()

--- /code ---

--- /task ---

--- task ---
Add to your existing code so that the camera preview starts when the sensor is activated, and stops when no motion is detected.

--- code ---
---
language: python
line_numbers: true
line_number_start: 1 
line_highlights: 8-12
---
from gpiozero import MotionSensor
from picamera import Camera

pir = MotionSensor(4)
cam = Camera()

while True:
	pir.wait_for_motion()
	print("Motion detected!")
    cam.start_preview()
    pir.wait_for_no_motion()
    cam.stop_preview()
--- /code ---
--- /task ---

--- task ---
Save your code, and run it. Test that the camera preview appears when the motion sensor is activated, and stops when the motion sensor is no longer active.
--- /task ---

