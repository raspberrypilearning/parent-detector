A Raspberry Pi Parent Detector
===============

How to use a Raspberry Pi to detect who's been in your room

![image](./images/cover.jpg "Cover Image")

A Raspberry Pi is so small that it can easily be hidden or concealed and that makes it the perfect tool for this kind of project.  The basic idea here is that we’re going to use motion detection to trigger video recording via the Raspberry Pi Camera Board.  You can then leave the Pi hidden in your room and see who's been caught on camera when you get home from School.

##Lesson objective
* Understand a Passive Infra Red motion sesnor
* Understand how to use the `picamera` Python module
* Understand how to record videos
* Understand how to play back videos

##Lesson outcome
*	To have built and tested a Raspberry Pi parent detector
*	Caught someone on camera
*	Gained experience in Python programming
*	Gained experience using the Raspberry Pi GPIO pins

##Time
*	1-2 hours

##Requirements
*	Raspberry Pi
*	Micro USB power adapter
*	An SD Card with Raspbian already set up through NOOBS
*	USB Keyboard
*	USB Mouse
*	HDMI cable
*	A Monitor or TV
*	Raspberry Pi Camera Board
*	PIR Motion Sensor Module (try [eBay](http://search.ebay.co.uk/pir+motion+sensor+module "eBay search"))
*	**Female** to **Female** jumper wires, at least 3 (try [eBay](http://search.ebay.co.uk/female+to+female+jumper+wires+solderless "eBay search"))

##Recommended
*	Camera Board 360 Gooseneck Mount (from [modmypi.com](https://www.modmypi.com/flexible-camera-mount "ModMyPi | RPi Camera Board 360 Gooseneck Mount"))

##Introduction - so what is a PIR module?

PIR stands for Passive Infra Red.  You’ve all seen these things before, they are tremendously common these days.  Most often found in the corners of rooms for burglar alarm systems.  All objects that are above absolute zero emit radiation in the form of infra red.  Infra red wavelengths are not visible to the human eye but they can be detected by the electronics inside one of these modules.

The sensor is regarded as passive because it doesn’t send out any signal in order to detect movement.  It adjusts itself to the infra red signature of the room it’s in and then watches for any changes.  Any object moving through the room will disturb the infra red signature and will cause a change to be noticed by the PIR module.

![image](./images/pir_module.png "PIR Motion Sensor Module")

We don’t need to worry about its inner workings.  What we’re interested in are those three pins on it.  We can connect those to the Raspberry Pi GPIO pins.  One is for +5 volts, one is for ground and the other is the sensor pin (the middle pin on our one).  That pin will receive power whenever motion is detected by the PIR module.  We can then see that happening on the Raspberry Pi and take action accordingly.

## Step 1: Setting Up your Pi
First check that you have all the parts you need to get your Raspberry Pi set up and working.

- Raspberry Pi
- Micro USB power adapter
- An SD Card with Raspbian already set up through NOOBS
- USB Keyboard
- USB Mouse
- HDMI cable
- A Monitor or TV

**Activity Checklist**

1.	Place the SD card into the slot of your Raspberry Pi. It will only fit one way so be careful not to break the card. 
2.	Next connect the HDMI cable from the monitor (or TV) to the HDMI port on the Pi and turn on your monitor. 
3.	Plug the USB keyboard and mouse into the USB slots on the Pi.
4.	Plug in the micro USB power supply and you should see some text appear on your screen.
5.  When prompted to login type:

    ```
    Login: pi
    Password: raspberry
    ```

##Step 2: Connect the PIR motion sensor

This should ideally be connected with the Raspberry Pi turned off for safety.  Use the following command to shut down the Pi.

`sudo halt`

Wait for the ACT (activity) LED to stop blinking before turning off the power.  Follow the instructions below to connect the PIR module to the Raspberry Pi.

![image](./images/pir_wiring.png "PIR to Pi wiring diagram")

Refer to the diagram above for pin numbers.  If you look closely at the pins on your PIR module you’ll see some white text on the PCB near the base of each one.  `VCC` is for +5 volts input.  Take one of the **female** to **female** jumpers and connect the VCC pin to pin 2 (red) on the Pi, this will make the Pi give 5 volts of power to the PIR module.  Use another jumper to connect `GND` on the module to pin 6 (black) on the Pi, this completes the circuit and allows current to flow back out of the module into ground.  Now do the same for the sensor pin `OUT`, you can use any of the green pins on the Pi for this but I am going to use pin number 7 (since it’s the first general purpose one).

**Note**: If you have a different PIR module to our one then your pin layout might be different, this is why I refer you to the labels `VCC` `GND` and `OUT`.

Turn the Pi back on and log in.

##Step 3: Test the PIR motion sensor

We're going to use the Python programming language to write some code that will detect movement and print out some text (we can extend the program to involve the Camera Board later on).  When movement is detected the PIR motion sensor applies power to its OUT pin which we have connected to GPIO pin 7 on the Pi.  So in our code we just need to continually check pin 7 to see if it has power or not.

If a pin has power we call this **HIGH** and if not we call it **LOW**.

The program is pretty simple.  We're first setting up the Raspberry Pi GPIO pins to allow us to use pin number 7 as an input (so it can detect when the PIR module sends power).  We need to continually check the pin for any changes so a `while True` loop is used for this.  This is an infinite loop so the program will just run forever unless we stop it manually with `Ctrl - C`.

We then use two Boolean (True or False) variables for the previous state and the current state of the pin, the previous state being what the current state was the previous time around the loop.  Inside the loop we compare the previous state to the current state to detect when they're different.  We don't want to keep displaying a message if there has been no change.

Firstly create a blank Python file with the following command.

`nano pirtest.py`

Enter or copy and paste the code below.

```python
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

prevState = False
currState = False

while True:
    time.sleep(.1)
    prevState = currState
    currState = GPIO.input(sensorPin)
    if currState != prevState:
        print "GPIO pin {0} is {1}".format(sensorPin, "HIGH" if currState else "LOW")
```

Press `Ctrl - O` to save and `Ctrl - X` to quit.

Next make the Python file executable and then you can run it.

```
chmod +x pirtest.py
sudo ./pirtest.py
```

If you get an error saying `RuntimeError: No access to /dev/mem` it means you forgot to use `sudo`.  You must run programs that access the GPIO as root and `sudo` does this for you.  Think of it as super-user-do.  

If you start moving or waving it will go HIGH.  Keep on waving and it will stay HIGH and only go back to LOW if you keep still again.  If this is what you have then everything is working correctly.  If not then something is wrong and you need to go back and troubleshoot.

```
GPIO pin 7 is HIGH
GPIO pin 7 is LOW
GPIO pin 7 is HIGH
```

Press `Ctrl – C` when you want to exit.

![image](./images/pir_potentiometers.png "PIR potentiometers")

On the PIR module you should have two orange coloured components that look like they take a phillips screwdriver (see above).  These things are called *potentiometers* and they allow you to adjust the sensitivity of the sensor and the detection time.  I would suggest to have sensitivity set to max and time to min, the choice is yours though.
