# Parent Detector {intro}

In this project you will use a Raspberry Pi, a picamera and a passive infrared motion sensor to create a parent detector, that can record video of anyone who enters your room.

## PIR motion sensors {mini}
[about_pir.md](about_pir.md)

## Connecting a PIR {mini}
{var1} = 4

[connect_pir.md](connect_pir.md)

## Setting up a picamera {mini}
[connect_camera.md](connect_camera.md)

## Triggering the camera on movement

Now that you have a working PIR and a Picamera, you can write some code to trigger the camera when ever motion is detected.

The code you wrote to test the PIR sensor can be adapted for this. In the test code, `Motion Deteceted!` was printed out to the shell whenever the PIR was triggered. This time you want the camera to start taking video.

Here's a little script that will tell the camera to start recording video.

``` python
from picamera import PiCamera
from time import sleep

camera = PiCamera()
filename = '/home/pi/Desktop/myvid.h264'

camera.start_recording(filename)
sleep(5)
camera.stop_recording()
```

### Task 1

Can you use this code, along with your PIR test code so that the camera starts recording when motion is detected.

### Code {hint}{1}
You can start by importing the modules and setting up the `camera` and `pir` objects. You'll also need a filename for the video.

``` python
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
filename = 'home/pi/Desktop/my_vid.h264
```

Now you need 4 more lines.
1. Wait for the PIR to be triggered
1. Start the camera recording
1. Pause the program for a few seconds
1. Stop the camera from recording

### Code {hint}{2}
Still stuck - here's the full code.
``` python
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
filename = 'home/pi/Desktop/my_vid.h264

pir.wait_for_motion
camera.start_recording(filename)
sleep(5)
camera.stop_recording()
```

## Stopping the camera when there's no motion

You could alter this code, so that rather than using a `sleep` the camera stops recording when there is no motion detected.

Using the following line, a python script would pause until no motion was detected by the PIR.

``` python
pir.wait_for_no_motion()
```

### Task 2

Can you use this code so that your camera stops recording when no motion is detected? You won't need the sleep anymore.

### Code {hint}{1}
The two lines you need to stop the camera recording when there is no motion are:

``` python
pir.wait_for_no_motion()
camera.stop_recording()
```

Can you add these into you code in the correct place, and remove the `sleep` command.

### Code {hint}{2}
Still stuck - here's the full code

``` python
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
filename = '/home/pi/Desktop/my_vid.h264'

pir.wait_for_motion
camera.start_recording(filename)
pir.wait_for_no_motion()
camera.stop_recording()
```

## Time stamping a file {mini}
[time_stamp.md](time_stamp.md)

## Adding a time stamp to your video

### Task 3

Now you know how to add a timestamp, this can be added to your code.
Instead of setting the `filename` variable to `my_vid.h264`, it can be set to the timestamp that you learned about in the previous section.

### Code {hint}{1}

``` python
path = '/home/pi/Desktop/'
filename = 'datetime.now().isoformat()
extension = '.h264'
```

### Code {hint}{2}
``` python
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
path = '/home/pi/Desktop/'
filename = 'datetime.now().isoformat()
extension = '.h264'

pir.wait_for_motion
camera.start_recording(path + filename + extension)
pir.wait_for_no_motion()
camera.stop_recording()
```

## Playing video on he Raspberry Pi {mini}
[play_video.md](play_video.md)

## Adding a loop

### Task 4

At the moment your code runs once, and then ends. This is great to catch an intruder out when they first enter your room, but not to find out what they're doing in there. If they stop moving for a second or two, the recording will stop and the program will end.

You can add a while loop into your code to make sure that it constantly watches out for movement and captures video.

If you need help with this, then you can check out the [mini project on while loops](while_loops.md).

### Code {hint}
``` python
from gpiozero import MotionSensor
from picamera import PiCamera
from time import sleep

pir = MotionSensor(4)
camera = PiCamera()
path = '/home/pi/Desktop/'
filename = 'datetime.now().isoformat()
extension = '.h264'

while True:
    pir.wait_for_motion
    camera.start_recording(path + filename + extension)
    pir.wait_for_no_motion()
    camera.stop_recording()
```
