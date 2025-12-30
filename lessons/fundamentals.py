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

# Conditional Statements
temperature = 53
if temperature > 30:
    print(f"it is warm {temperature}%")
elif temperature > 10:
    print("It is nice")
else:
    print("It is cold")
print("Evaluated")

# Ternary Operators
age = 15
message = "Eligible" if age >= 18 else "Not Eigible"
print(message)


# Logical Operators
# and
# or
# not
#
#
name = input("What's your name: ")
isGoodCredit = True
isHighValue = False
isStudent = False
# With and both conditions have to be true
# if isGoodCredit and isHighValue:
#     print(f"{name} is Eligible")
# else:
#     print(f"{name} is Not eligible")


# # With or one of the conditions have to be true
# if isGoodCredit or isHighValue:
#     print(f"{name} is Eligible")
# else:
#     print(f"{name} is Not eligible")


# # With not the inverse has to be true


# if not isStudent:
#     print("Not a registered student")
# else:
#     print("A registered student")


# This is awesome, this logic reads like engliish
if (isHighValue or isGoodCredit) and not isStudent:
    print(f"{name.capitalize()} Is Eligible")
else:
    print(f" {name.capitalize()} Is Not Eligible")


# Conditional operators can also be chained like so
# This code is the same as this
# if age >= 18 and age < 65:
#   print("Eligibilty check passed")
age = 22
if 18 <= age < 65:
    print("Eligibilty check passed")
