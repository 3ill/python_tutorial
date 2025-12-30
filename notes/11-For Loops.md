---
title:
tags:
type:
author:
creationDate:
alias:
---
>[!summary]
>_This note outlines how to use for loops in python_

Here's a simple code snippet of a for loop.
```python
for number in range(5):
    number += 1
    print(f"attempt {number}")

```

>[!note]
>range is a special python function that states the amount of times code in the for loop should run for


**Range also accepts a range of values, so we can set a start value and an end value. the last value is non inclusive. in this  example the print statement will be executed 5 times.**

```python
for number in range(1, 6):
    print(f"attempt {number},", (number) * ".")
```

**Range also accepts a third option which is the step**
```python
# You can also pass a step, this number will be added to the processing number in this case it will be 1 + 2 = 3 + 2 = 5 ....
for number in range(1, 6, 2):
    print(f"attempt {number},", (number) * ".")

```

## For else statement
A for else statement is used when you want to perform an operation if the code in the for loop never executes. this is similar to the default statement when using `switch` statements in Javascript
```python
isSuccessful = False
for number in range(1, 5):
    if isSuccessful:
        print("Success")
        break
else:
    print("Attempted to send the message 4 times")
```



## Nested loops
When working with nested loops, the inner loop is processed first before the outer loop.
```python
# When working with nested loops, the inner loop executes first.
# In this case x is 0 and y is looped through , Then x is 1 and y is looped through
# The result looks like (0, 0), (0, 1), (0, 2).... (1, 0), (1, 1), (1, 2)... (2, 0)
for x in range(5):
    for y in range(4):
        print(f"({x}, {y})")
```

>[!important]
>It is important to know that `range` is not the only iterable type in python. `list` and `string` are also iterable and you can make a custom object and make it iterable as well



##### Go Back: [[10-Comparison & Conditional Statements]]
##### Up Next: [[12-While Loops]]
