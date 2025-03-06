class MaxList:
    def __init__(self):
        self.list = []
        self.current_max = None

    def append(self, number):
        self.list.append(number)
        
        if self.current_max is None or number > self.current_max:
            self.current_max = number

    def max(self):
        return self.current_max

if __name__ == "__main__":
    numbers = MaxList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)
    print(numbers.max()) # 3

    numbers.append(8)
    numbers.append(5)
    print(numbers.max()) # 8