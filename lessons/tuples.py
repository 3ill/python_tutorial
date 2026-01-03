# Tuples are immutable, the code below will throw an error
numbers = (1, 2, 3, 4, 5, 6)
# numbers[0] = 3


# Unpacking is a core feature of python that allows you to instantly assign elements in a tuple or array to variables
a, b, c, d, e, f = numbers

print(a, b, c, d, e, f)
