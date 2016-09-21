## Time stamping files in Python

Quite often you want to add a time or date stamp to a filename. This is particularly useful when writing out lots of files using Python, so that the files don't overwrite each other. It can also easily help you know when a particular file was created.

First, let's have a look at some basic code to write out a simple text file in Python. Open `Python 3 (IDLE)` from the `Programming` section of the `Menu`. Then click on `File` and then `New File`.

Write the following two lines and then run your program using `F5`

``` python
with open('home/pi/Desktop/my_file.txt',`w`) as f:
    f.write('Hello')
```

The `home/pi/Desktop` part of the first line tells Python which directory to save in. In this case you're saving to yout `Desktop`. The `my_file.txt` is the name of the file.

The `'w'` argument is telling your program that you want to be able to write into the file.
If you double click the file that appears on your desktop, it should open up in a text editor and you should see the word `Hello`.

If you alter the code, as shown below and then rerun it, the old file will be written over. The file will now say `Goodbye`

``` python
with open('home/pi/Desktop/my_file.txt',`w`) as f:
    f.write('Hello')
```

So how can you add a timestamp to the file? You can use the `datetime` module for this and create some useful objects to fetch timestamps. Try the following in the shell:

``` python
>>> from datetime import datetime
>>> datetime.now().day
```

As you can see, this gives you the current day as a number.
You can use similar commands to get the year, month, minute as well

``` python
>>> datetime.now().year
>>> datetime.now().month
>>> datetime.now().minute
```

Even more usefully, we can get the current date and time as a string in what is known as an **ISO 8601** format.

``` python
datetime.now().isoformat()
```

This string could be really useful for date and time stamping our files. We could write code as follows:

``` python
from datetime import datetime

path = '/home/pi/Desktop/'
filename = datetime.now().isoformat()
extension = '.txt'

with open(path + filename + extension, 'w') as f:
    f.write('Hello')
```

Now each time you run the code, a new file will be created, because the filename keeps changing according to the time the file was run.
