class ChangeList:
    def __init__(self):
        self.numbers = []
        self.total_change = 0

    def append(self, number):
        self.numbers.append(number - self.total_change)

    def get(self, index):
        return self.numbers[index] + self.total_change

    def change_all(self, amount):
        self.total_change += amount

if __name__ == "__main__":
    numbers = ChangeList()

    numbers.append(1)
    numbers.append(2)
    numbers.append(3)

    print(numbers.get(0)) # 1
    print(numbers.get(1)) # 2
    print(numbers.get(2)) # 3

    numbers.change_all(2)
    print(numbers.get(0)) # 3
    print(numbers.get(1)) # 4
    print(numbers.get(2)) # 5

    numbers.append(8)
    numbers.change_all(-1)
    print(numbers.get(0)) # 2
    print(numbers.get(1)) # 3
    print(numbers.get(2)) # 4
    print(numbers.get(3)) # 7