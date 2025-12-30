---
title: 
tags: 
type: 
author: 
creationDate: 
alias:
---

>[!summary] 
>_This note outlines concepts of comparison and conditional statements in python_


#### Comparison
These are your regular `<`  `>` operators.  This is very similar to the way you use comparison operators in `JavaScript`
```python
# Comparsion Operators
isGreater = 10 > 3
print(isGreater)

isLessThan = 10 < 3
print(isLessThan)

isGreaterOrEqual = 10 >= 3
print(isGreaterOrEqual)

isEqual = 10 == 10
print(isEqual)

isNotEqual = 10 != 10
print(isNotEqual)


# Comparison with string
print(f"{'bag' > 'apple'}")
```


#### Conditionals
These are your `if` `else` `elif` statements
##### If statement
```python
temperature = 53
if temperature > 30:
    print(f"it is warm {temperature}%")
print("Evaluated")
```

>[!important] 
>The none indented print statement will always run regardless of if the indented block is run or not

##### elif and else statements
```python
temperature = 53
if temperature > 30:
    print(f"it is warm {temperature}%")
elif temperature > 10:
    print("It is nice")
else:
    print("It is cold")
print("Evaluated")
```

___
#### Ternary Operators
This is particular if you are trying to set a value based on a condition
```python
age = 15
message = "Eligible" if age >= 18 else "Not Eigible"
print(message)
```

#### Logical operators
Logical operators are `and`,  `or` , `not` . these are similar to logical operators in `Javascript`
```python
name = input("What's your name: ")
isGoodCredit = True
isHighValue = False
# With and both conditions have to be true
if isGoodCredit and isHighValue:
    print(f"{name} is Eligible")
else:
    print(f"{name} is Not eligible")


# With or one of the conditions have to be true
if isGoodCredit or isHighValue:
    print(f"{name} is Eligible")
else:
    print(f"{name} is Not eligible")
    
    
# With not the inverse has to be true
isStudent = False

if not isStudent:
    print("Not a registered student")
else:
    print("A registered student")


# This is awesome, this logic reads like engliish
if (isHighValue or isGoodCredit) and not isStudent:
    print("Is Eligible")
else:
    print("Is Not Eligible")
```

>[!important] 
>In python, logical operators are short circuit, this means that when the interpreter meets a false statement in a conditional it exits the condtional


### Chaining comparison operators
Conditionals can also be chained in python, in my opinion it is cleaner than JavaScript
```python
# Conditional operators can also be chained like so
# This code is the same as this
# if age >= 18 and age < 65:
#   print("Eligibilty check passed")
age = 22
if 18 <= age < 65:
    print("Eligibilty check passed")
```


##### Go Back: [[09-Number manipulation]]
##### Up Next: [[11-For Loops]]