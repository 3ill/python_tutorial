# Function with arguments
# This function is performative, it does not return any value
#
def greet(_name: str):
    print(f"Hello {_name}")


# This is not just performative
def get_greeting(_name: str):
    return f"Hi {_name}"


my_greeting = get_greeting("Chike")
print(my_greeting)


# Here _by is optional, when no value is passed to the _by params it defaults to 10
def increment(_value: int, _by: int = 10):
    return _value + _by


print(increment(2))


# Multiple optional params
# When the wild card is prefixed in front of a param, it means multiple arguments can be passed in and the type resolves to a tupule and it is iterable
def multiply(*numbers: int):
    print(numbers)
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(1, 2, 3, 4, 5))
