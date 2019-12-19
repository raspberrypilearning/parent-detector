--- challenge ---

## Challenge: stealth mode

You have completed your parent detector, but why not try taking it to the next level by using it in stealth mode?

- You could disable the red LED on the camera board which normally comes on when you start your Python program.

    --- hints ---

    --- hint ---
    This can be done by adding a command to the Raspberry Pi configuration file, called `config.txt`, found in `boot` folder.
    --- /hint ---

    --- hint ---
    Open a terminal window and enter the following command to begin editing the `config.txt` file:

    ```bash
    sudo nano /boot/config.txt
    ```

    Add the following line to the end of the file:

    ```bash
    disable_camera_led=1
    ```

    Press `Ctrl + O` to save, and `Ctrl + X` to quit. The changes will only take effect after a reboot - type the following command into the terminal to do this:

    ```bash
    sudo reboot
    ```

    --- /hint ---
    --- /hints ---

- The camera preview might give away to your intruders that they have been spotted. Can you remove the camera preview code from your script?

--- /challenge ---
