# import inheritance
from inheritance import RequestHandler
from utils.util import SortNumbers

new_handler = RequestHandler("https://modules.com")
path = new_handler.get_url("login")

print(path)


sorter = SortNumbers()
print(f"Max number => {sorter.find_max()}")
