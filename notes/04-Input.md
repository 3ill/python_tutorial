---
title: Input
tags:
  - code
  - note
  - python
type: note
author: 3ilBaby
creationDate: 
aliases:
---

> [!NOTE] Overview
> This note showcases how the input function works


### What are input functions
This  is a way to request data from the user interacting with your program.  Inputs can be assigned to variables and are returned as strings. 

```python
# Inputs

name = input("Enter your name: ")
print(f"welcome {name}");

```


Inputs are returned as strings, so when used to accept numbers, it is important to typecast

```python
item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))

print(f"the cost of {quantity} {item}s is {price * quantity}");
```

