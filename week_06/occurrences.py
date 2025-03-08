class OccurrenceTracker:
    def __init__(self):
        self.number_counts = {}
        self.occurrence_counts = {}

    def append(self, number):
        if number in self.number_counts:
            old_count = self.number_counts[number]
            self.occurrence_counts[old_count] -= 1
            if self.occurrence_counts[old_count] == 0:
                del self.occurrence_counts[old_count]
            self.number_counts[number] = old_count + 1
        else:
            self.number_counts[number] = 1

        new_count = self.number_counts[number]
        if new_count in self.occurrence_counts:
            self.occurrence_counts[new_count] += 1
        else:
            self.occurrence_counts[new_count] = 1

    def count(self):
        return len(self.occurrence_counts)

if __name__ == "__main__":
    tracker = OccurrenceTracker()

    tracker.append(1)
    tracker.append(2)
    tracker.append(1)
    tracker.append(3)
    print(tracker.count()) # 2

    tracker.append(2)
    tracker.append(3)
    print(tracker.count()) # 1

    tracker.append(2)
    tracker.append(3)
    tracker.append(3)
    print(tracker.count()) # 3

    tracker = OccurrenceTracker()
    total = 0
    for i in range(10**5):
        tracker.append(i % 100 + 1)
        total += tracker.count()
    print(total) # 198901