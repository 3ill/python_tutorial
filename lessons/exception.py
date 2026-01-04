def get_input():
    try:
        age = int(input("Age: "))
        print(age)
    except Exception as e:
        print(f"An Error occurred, {e}")


get_input()
