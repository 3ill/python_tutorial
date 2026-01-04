class MakeRequest:
    # The `__init__` method is a special method (the constructor) that gets called when you create a new `MakeRequest` object
    def __init__(self) -> None:
        self.url = "https://example.com"

    def get_url(self, _endpoint: str):
        return f"{self.url}/{_endpoint}"


request_handler = MakeRequest()
request_handler.url = "https://new.example.com"
print(request_handler.url)

path = request_handler.get_url("chike")
print(path)


class Person:
    def __init__(self, _name: str) -> None:
        self.name = _name

    def talk(self):
        print(f"i am talking to {self.name}")


new_person = Person("Winifred")
new_person.talk()
