class SortNumbers:
    def __init__(self) -> None:
        self.numbers = [1, 3, 6, 6, 9]
        self.max = 0
        self.min = 1

    def find_max(self):
        for number in self.numbers:
            if number > self.max:
                self.max = number
        return self.max

    def find_min(self):
        for number in self.numbers:
            if number < self.min:
                self.min = number
        return self.min
