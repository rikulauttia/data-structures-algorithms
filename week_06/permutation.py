class PermutationTracker:
    def __init__(self):
        self.numbers = set()
        self.size = 0
        self.sum = 0
        self.max_number = 0

    def append(self, number):
        self.numbers.add(number)
        self.size += 1
        self.sum += number
        self.max_number = max(self.max_number, number)

    def check(self):
        expected_sum = self.size * (self.size + 1) // 2
        return (self.sum == expected_sum and 
                self.size == len(self.numbers) and 
                self.max_number == self.size)

if __name__ == "__main__":
    tracker = PermutationTracker()

    tracker.append(1)
    print(tracker.check()) # True

    tracker.append(4)
    print(tracker.check()) # False

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(3)
    print(tracker.check()) # True

    tracker.append(2)
    print(tracker.check()) # False

    tracker.append(5)
    print(tracker.check()) # False