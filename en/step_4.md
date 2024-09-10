## Test the PIR motion sensor

We're going to write some code to print out "Motion detected!" when the PIR sensor detects movement.

--- task ---
Open **Thonny**, create a new file and save it as `parent_detector.py`.
--- /task ---

--- task ---
Write some code to set up your PIR sensor on **GPIO 4**:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1
---
from gpiozero import MotionSensor

pir = MotionSensor(4)
--- /code ---
--- /task ---

--- task ---
Add some more code so that when the PIR sensor detects motion, "Motion detected!" is displayed on the screen:

--- code ---
---
language: python
line_numbers: true
line_number_start: 1 
line_highlights: 4-5
---
from gpiozero import MotionSensor

pir = MotionSensor(4)
pir.wait_for_motion()
print("Motion detected!")
--- /code ---
--- /task ---

--- task ---

Save your code, and click on **Run** to run it. Wave your hand in front of the motion detector and you should see the words `Motion detected!` appear on the screen.

--- /task ---

At the moment your code only detects movement once and then the program ends. 

--- task ---

Add an **infinite loop** to keep checking for motion, then run your code again. 

--- code ---
---
language: python
line_numbers: true
line_number_start: 1 
line_highlights: 5-7
---
from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	print("Motion detected!")
--- /code ---
--- /task ---

Your code will now print `Motion detected!` every time the sensor is triggered. To exit your program you can click on **Stop**.
