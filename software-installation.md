## Software Installation

You'll need to be online to install packages.

First update and upgrade your system. Enter the following commands in to the terminal:

```bash
sudo apt-get update
sudo apt-get upgrade
```

Now install the packages you'll need:

```bash
sudo apt-get install python3-picamera
```

Test you have everything you need by entering the following command:

```bash
sudo python3 -c "import picamera"
```

This should bring you back to the command prompt with no errors. If you get an error saying `No module named picamera` then check you entered the commands above correctly.
