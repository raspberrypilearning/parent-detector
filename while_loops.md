## While loops

A loop will run the same few lines of code several times.
A While loop will run the code within it as long as a condition is `True`

The format for a while loop is as follows:

``` python
while condition:
    run this line
    then run this line
```

For instance, we could write code like this:

``` python
while 6 == 6:
    print('6 is equal to 6')
```

As `6 == 6` is always `True` this loop would run forever.

This loop however:

``` python
while 6 == 7:
    print('6 is equal to 7')
```

will never run, as `6 == 7` is always `False`

We can make loops where the condition starts off as being `True` and then becomes `False` after a few iterations.

``` python
foo = 0
while foo < 10:
    print('foo is less than 10')
    foo += 1
```

In this while loop, the condition starts off as `True` as `foo` is `0` which is definetley less than `10`. Each time through the loop though, `foo` increases by 1. Eventually it reaches `10` and the condition `foo < 10` is `False`, so the loop stops.

Sometimes we want infinite loop, that just runs until we manually stop a program. There are many ways of doing this in python. You've already written just such a loop with the `while 6 == 6:` loop.

As `6 == 6` is really just the same as saying `True`, it's easier and considered better practice to simply write:

``` python
while True:
    print('Endless loop')
```

