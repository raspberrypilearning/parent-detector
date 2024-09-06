## Test the PIR motion sensor

We're going to write some code to print out "Motion detected!" when the PIR sensor detects movement.

--- task ---

Open **Thonny**, create a new file and save it as `parent_detector.py`.

--- /task ---

--- task ---

Write some code to set up your PIR sensor on **GPIO 4**.

Here is the full code:

--- code ---
---
language: python
filename: parent_detector.py
line_numbers: true
line_number_start: 1
---
from gpiozero import MotionSensor

pir = MotionSensor(4)
--- /code ---


--- /task ----

--- task ---

Add some more code so that when the PIR sensor detects motion, "Motion detected!" is displayed on the screen:

--- code ---
---
language: python
filename: parent_detector.py
line_numbers: true
line_number_start: 1 
highlight_lines: 5,6
---
from gpiozero import MotionSensor

pir = MotionSensor(4)

pir.wait_for_motion()
print("Motion detected!")

--- /code ---

--- /task ---

--- task ---

Save your code, and click on **Run** to run it. You should see the words `Motion detected!` appear on the screen when the motion sensor is triggered.

--- /task ---

--- task ---

At the moment your code only detects movement once and then the program ends. Put your code inside an **infinite loop**: 

--- code ---
---
language: python
filename: parent_detector.py
line_numbers: true
line_number_start: 1 
highlight_lines: 5-7
---
from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	print("Motion detected!")

--- /code ---


--- /task ---

Python will keep waiting for a signal from the motion sensor and will print `Motion detected!` every time the sensor is triggered. To exit your program you can click on **Stop**.
