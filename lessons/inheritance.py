class MakeRequest:
    # The `__init__` method is a special method (the constructor) that gets called when you create a new `MakeRequest` object
    def __init__(self) -> None:
        self.url = "https://example.com"

    def get_url(self, _endpoint: str):
        return f"{self.url}/{_endpoint}"


class RequestHandler(MakeRequest):
    pass


handler = RequestHandler()

url = handler.get_url("login")
print(url)
