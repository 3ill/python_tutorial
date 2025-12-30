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


for x in range(5):
    for y in range(4):
        print(f"({x}, {y})")
