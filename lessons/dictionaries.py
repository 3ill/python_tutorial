# Dictionaries are data structures in python used to store key, value pairs
customer = {"name": "John Doe", "age": 28, "gender": "M"}

# Accesing keys values in dict
print(customer["age"])
print(customer.get("name", "Missing Person"))


# Mutating values and adding keys in dict
customer["name"] = "Chike Egbu"
customer["birthdate"] = "Apr, 23"


print(customer.get("name", "Missing Person"))

num_list = {"1": "One", "2": "Two", "3": "Three", "4": "Four"}


def convert_num(_num: str):
    return num_list[_num]


def deconstruct():
    arrayed_numbers = []
    numbers = input("Phone: ")
    for num in numbers:
        arrayed_numbers.append(convert_num(num))

    return arrayed_numbers


a, b, c, d = deconstruct()
print(a, b, c, d)


# Dummy db
#


user = {"firstName": "Chike", "lastName": "Egbu", "email": "chikeegbu@gmail.com"}
user_table = [user]


def validate_user(email: str, _phone: str):
    is_user_valid: bool = False
    for user in user_table:
        if user["email"].lower() == email.lower():
            is_user_valid = True
            user["phone_number"] = _phone
    print(user_table[0])
    return is_user_valid


is_valid = validate_user("chikeegbu@gmail.com", "123456")
print(f"is user valid: {is_valid}")
