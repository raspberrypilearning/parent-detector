## Record video in a file

Seeing the intruder on the screen in a camera preview while they are in the room isn't much help to you. Instead, let's record a video of the intruder which you can view later on when you get home.

--- task ---
Create a variable called `filename` inside your infinite loop to store the name of the video file.

--- code ---
---
language: python
filename: parent_detector.py
line_numbers: true
line_number_start: 1 
highlight_lines: 6
---
from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()
filename = "intruder.h264"

while True:
	pir.wait_for_motion()
	print("Motion detected!")
    camera.start_preview()
    pir.wait_for_no_motion()
    camera.stop_preview()
--- /code ---

In case you are wondering, `.h264` is the video format.
--- /task ---

--- task ---
Find the line of code that starts the camera preview, and replace it with a line of code that starts a video recording.

--- code ---
---
language: python
filename: parent_detector.py
line_numbers: true
line_number_start: 1 
highlight_lines: 11
---
from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()
filename = "intruder.h264"

while True:
	pir.wait_for_motion()
	print("Motion detected!")
    camera.start_recording(filename)	
    pir.wait_for_no_motion()
    camera.stop_preview()
--- /code ---

--- /task ---

--- task ---
Find the line of code stopping the camera preview, and replace it with a line of code stopping recording.

--- hints ---

--- hint ---
Look at the line of code you used to start recording, and see if you can use it to work out the code to stop recording.
--- /hint ---

--- hint ---
Here is the finished code:

--- code ---
---
language: python
filename: parent_detector.py
line_numbers: true
line_number_start: 1 
highlight_lines: 11
---
from gpiozero import MotionSensor
from picamera import PiCamera

pir = MotionSensor(4)
camera = PiCamera()
filename = "intruder.h264"

while True:
	pir.wait_for_motion()
	print("Motion detected!")
    camera.start_recording(filename)	
    pir.wait_for_no_motion()
	camera.stop_recording()
--- /code ---

--- /hint ---
--- /hints ---
--- /task ---

--- task ---
Save your program, and run it. Check that a file called `intruder.h264` appears in the same folder as your `parent-detector.py` file.
--- /task ---

--- challenge ---
Every time a new intruder triggers the motion sensor, the video file will be overwritten. If you have lots of pesky parents or siblings intruding into your room, you want to keep videos of all of them. Can you write some code to automatically find out the current date and time, and add it to the name of the video file? Then each video you record will have a different filename.

[[[generic-python-timestamps]]]

--- /challenge ---
