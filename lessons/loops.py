# range is a special python function that states the amount of times code in the for loop should run for
for number in range(1):
    print(f"attempt {number},", (number) * ".")


# You can also pass a start and end value, the last value is non inclusive, the code will only run 5 times in this case
for number in range(1, 6):
    print(f"attempt {number},", (number) * ".")
