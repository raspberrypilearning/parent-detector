## Record video in a file

Seeing the intruder on the screen in a camera preview while they are in the room isn't much help to you. Instead, you can record a video of the intruder which you can view later on when you get home.

--- task ---
Find the line of code that starts the camera preview, and replace it with a line of code that starts a video recording.

--- code ---
---
language: python
line_numbers: true
line_number_start: 8
highlight_lines: 11
---
while True:
	pir.wait_for_motion()
	print("Motion detected!")
    cam.start_recording("intruder.mp4")	
    pir.wait_for_no_motion()
    cam.stop_preview()
--- /code ---

--- /task ---

--- task ---
Find the line of code stopping the camera preview, and replace it with a line of code to stop the recording.

--- code ---
---
language: python
line_numbers: true
line_number_start: 11
highlight_lines: 13
---
    cam.start_recording("intruder.mp4")	
    pir.wait_for_no_motion()
    cam.stop_preview()
--- /code ---
--- /task ---

--- task ---
Save your program, and run it. Check that a file called `intruder.mp4` appears in the same folder as your `parent-detector.py` file. Double click on the file to play it.
--- /task ---


