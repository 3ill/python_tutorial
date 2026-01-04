# Exceptions are similar to the try, catch pattern in Javascript.
# except is the catch block and Exception is the error that is being returned
def get_input():
    try:
        age = int(input("Age: "))
        print(age)
    except Exception as e:
        print(f"An Error occurred, {e}")


get_input()
