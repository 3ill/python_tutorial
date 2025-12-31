# This returns a new list with items starting from the second index
names = ["John", "Jane", "Joseph", "Chike", "Mary", "Obinna"]
print(names[2:])

# List can also be directly modified
names[0] = "Jon"
print(names)

numbers = [1, 2, 3, 4, 5, 8, 20]
largest_num = 0

for number in numbers:
    if number > largest_num:
        largest_num = number
        print(f"New largest number is now {largest_num}")
print(f"final largest number is {largest_num}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
second_element_in_inner_list = matrix[0][2]
print(f"The second element in inner list is {second_element_in_inner_list}")

# Items in 2D lists can also be mutated
matrix[0][2] = 5

for row in matrix:
    for item in row:
        print(item)
