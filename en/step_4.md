## Test the PIR motion sensor

We're going to write some code to print out "Motion detected!" when the PIR sensor detects movement.

--- task ---

Open Mu, create a new file and save it as `parent_detector.py`.

[[[mu-open]]]

--- /task ---

--- task ---

Set up your PIR sensor on **GPIO 4**.

--- hints ---

--- hint ---

You will need to use the `gpiozero` library to create a `MotionSensor` that is connected to the correct GPIO pin.

--- /hint ---

--- hint ---

Here is the full code:

--- code ---
---
language: python
filename: parent_detector.py
line_numbers: true
line_number_start: 1
highlight_lines: 
---
from gpiozero import MotionSensor

pir = MotionSensor(4)

--- /code ---

--- /hint ---

--- /hints ---

--- /task ----

--- task ---

Add some more code so that when the PIR sensor detects motion, "Motion detected!" is displayed on the screen.

--- hints ---

--- hint ---

Look at the documentation for [GPIO Zero](https://gpiozero.readthedocs.io/en/stable/api_input.html#motion-sensor-d-sun-pir) to find out how to use the `wait_for_motion()` method.

--- /hint ---

--- hint ---

Here is the code:

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

--- /hint ---

--- /hints ---

--- /task ---

--- task ---

Save your code, and click on **Run** to run it. You should see the words `Motion detected!` appear on the screen when the motion sensor is triggered.

--- /task ---

--- task ---

At the moment your code only detects movement once and then the program ends. Put your code inside an **infinite loop** so that Python will keep waiting for a signal from the motion sensor and will print `Motion detected!` every time the sensor is triggered. To exit your program you can click on **Stop**.

[[[generic-python-while-true]]]

--- hints ---

--- hint ---

The code for an infinite loop is shown below. Any lines of code to be repeated should be __indented__ within the loop.

```python
while True:
```

--- /hint ---

--- hint ---

You need to put your code to detect motion, inside a loop.

--- code ---
---
language: python
filename: parent_detector.py
line_numbers: true
line_number_start: 1 
highlight_lines: 5,6,7
---
from gpiozero import MotionSensor

pir = MotionSensor(4)

while True:
	pir.wait_for_motion()
	print("Motion detected!")

--- /code ---

--- /hint ---

--- /hints ---

--- /task ---

