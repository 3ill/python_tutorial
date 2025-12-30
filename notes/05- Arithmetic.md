---
title: arithmetic operators
tags:
  - code
  - note
  - research
type: note
author: 3ilBaby
creationDate: 
aliases:
---

#### Assignment Operators

This is an augmented assignment operator. it adds one to the previously assigned variable. It is basically a short form of writing 
`friends = friend + 1`
```Python
friend = 0
friends += 1;
```

This can be done with subtraction, division and multiplication too. 

```Python
friend -= 3
friend *= 3
friend /= 3
```

##### Exponents
```Python
friend **=2
```



##### In built Math functions 
Python also has inbuilt math functions baked in similarly to Javascript
```Python 
result = round(x)
result = pow(4, 5);
```


We can also import the `math` library to do some more complex arithemetic

```Python
import math

radius = float(input("Enter a radius of the circle: "))

area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}cm^2")
```



##### Up Next: [[06-Double Underscore]]
##### Back: [[04-Input]]
