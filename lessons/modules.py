# import inheritance
from inheritance import RequestHandler
from utils import util

new_handler = RequestHandler("https://modules.com")
path = new_handler.get_url("login")

print(path)


sorter = util.SortNumbers()
print(f"Max number => {sorter.find_max()}")
