
# String Manipulation
# This returns the length of the string
newString = "I am learning python, i am liking it"
stringLength = len(newString)



# Slice
# This returns the first 3 characters
print(newString[0:3])


# Escape sequence
course = "Python \nProgramming"
print(course)


# Concatenation
# This will join the result of two strings
first = "Chike"
last = "Egbu"

full = first + " " + last
print(full)


# Formatted Strings
formatted_full = f"{first} {last}"
print(formatted_full)

# Find
print(first.find("C", 0))

random_string = " Chike Egbu "
print(random_string.strip())


print("Chike" in random_string)

print("Chike" not in random_string)
