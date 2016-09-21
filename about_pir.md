## About the Passive Infrared (PIR) motion sensor

In this project, we are going to be using a Passive Infrared (PIR) motion sensor. You have probably seen these before: they are often used in burglar alarm systems (the sensors placed in the corners of rooms are typically PIR ones). All objects whose temperatures are above absolute zero emit infrared radiation. Infrared wavelengths are not visible to the human eye, but they can be detected by the electronics inside one of these modules.

The sensor is regarded as passive because it doesn't send out any signal in order to detect movement. It adjusts itself to the infra red signature of the room it's in and then watches for any changes. Any object moving through the room will disturb the infra red signature, and will cause a change to be noticed by the PIR module.

![](images/pir_module.png)

We don't need to worry about the inner workings of the motion sensor. What we're interested in are the three pins on it, that can be used to connect it to the Raspberry Pi.
