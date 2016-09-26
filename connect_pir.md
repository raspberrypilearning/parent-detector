## Connect the PIR motion sensor

Using three female-to-female jumper cables, you'll need to connect each of the PIR sensor's connectors to the appropriate pins on the Raspberry Pi. Don't rely on the diagram, for which pin is which though; check the labels on the PIR.

1. Connect the one labelled `VCC` on the PIR sensor to the 5V pin on the Raspberry Pi. This provide power to the PIR sensor.
1. Connect the one labelled `GND` to a ground pin on the Raspberry Pi. This completes the circuit.
1. Connect the one labelled `OUT` to GPIO pin {var1}. This pin will output a voltage when motion is detected, that can then be received by the Raspberry Pi

![](images/PIR_connect_1.gif)
![](images/PIR_connect_2.gif)

![](images/pir_wiring.png)

With the PIR connected you can now write a little bit of code to test that it is working.
Open up Python 3 (IDLE) from the `Menu` > `Programming` menu. Then you can create a new file by clicking on `File` > `New File`, where you can write your code.

First you will need to import a `MotionSensor` object from the `gpiozero` module. This will let you read signals from the motion sensor using Python.

``` python
from gpiozero import MotionSensor
```

The motion sensor was attached to pin {var1}, so you need to tell your program that is the pin to monitor.

``` python
pir = MotionSensor({var1})
```

Now with two more lines of code, you can tell the program to wait until motion has been detected and then print a message.

``` python
pir.wait_for_motion()
print('Motion detected')
```

### Full code {hint}

``` python
from gpiozero import MotionSensor
pir = MotionSensor({var1}

pir.wait_for_motion()
print('Motion detected!')
```

Save your file and press `F5` to run it.

Everytime the PIR detects motion, you should see the words `Motion detected!` appear in the IDLE shell and then your program will quit.

![](images/pir_potentiometers.png)

On the PIR module you should see two orange components with sockets that fit a Phillips screwdriver (see above). These are called potentiometers: they allow you to adjust the sensitivity of the sensor and the detection time. You should begin by setting the sensitivity to max and the time to min, but you can vary this later if you wish.
