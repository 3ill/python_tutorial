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


# List Methods
new_numbers = [5, 2, 10, 1, 17, 10]
# append adds to the end of the list
new_numbers.append(21)

# insert accepts index and value as param
new_numbers.insert(1, 3)

# remove will remove the item passed as argument from the list
# It will throw an error if the element does not exist in the list
new_numbers.remove(21)
print(new_numbers)


# By default, pop will remove and return the last item in the list but it also accepts an index as args.
# If index is provided, it will remove and return the element at that index
# popped_index = new_numbers.pop()
# print(f"removed {popped_index}")

index = new_numbers.index(17)
print(f"17 is at index {index}")

# clear will empty the list
# new_numbers.clear()
# print(new_numbers)

# This will return a boolean
# This is the best whenn trying to check for the existence of an item in a list
print(17 in new_numbers)

# The count method accepts a param of an element in the lists and returns the number of items that element appears in the list
print(new_numbers.count(10))

# The sort method sorts a list in ascending order, the reverse sorts a list in descending order
new_numbers.sort()
new_numbers.reverse()
print(f"sorted lists {new_numbers}")

# The copy returns a copy of the list as a new list
# The new lists is independent of the original list, changes made to the original list does not affect the copy
new_numbers2 = new_numbers.copy()
new_numbers.append(30)


print(new_numbers)
print(f"copy: {new_numbers2}")


duplicated_lists = [1, 2, 2, 3, 4, 6, 9, 6, 9]


def remove_duplicates():
    for item in duplicated_lists:
        if duplicated_lists.count(item) > 1:
            duplicated_lists.pop(duplicated_lists.index(item))
            print(f"duplicate number found and removed {item}")
    else:
        print(f"duplicates processed successfully. new list {duplicated_lists}")


remove_duplicates()
