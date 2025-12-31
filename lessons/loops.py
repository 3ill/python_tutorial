# range is a special python function that states the amount of times code in the for loop should run for
# for number in range(1):
#     print(f"attempt {number},", (number) * ".")


# You can also pass a start and end value, the last value is non inclusive, the code will only run 5 times in this case
# for number in range(1, 6):
#     print(f"attempt {number},", (number) * ".")


# You can also pass a step, this number will be added to the processing number in this case it will be 1 + 2 = 3 + 2 = 5 ....
# for number in range(1, 6, 2):
#     print(f"attempt {number},", (number) * ".")


# Breaking out of the for loop
isSuccessful = False
for number in range(1, 5):
    if isSuccessful:
        print("Success")
        break
else:
    print("Attempted to send the message 4 times")

# Nested loops
# When working with nested loops, the inner loop executes first.
# In this case x is 0 and y is looped through , Then x is 1 and y is looped through
# The result looks like (0, 0), (0, 1), (0, 2).... (1, 0), (1, 1), (1, 2)... (2, 0)
for x in range(5):
    for y in range(4):
        print(f"({x}, {y})")


# While Loops
# While loops are used to perform evaluation while a condition holds true, on like a for statement, there are no iterables to iterate over
# number = 100
# while number > 0:
#     number //= 2
#     print(number)

# command = ""
# while command != "quit":
#     command = input(">").lower()
#     print(f"you typed {command}")


count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"We have {count} even numbers")
