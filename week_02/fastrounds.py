def count_rounds(numbers):
    n = len(numbers)
    
    positions = {}
    for i, num in enumerate(numbers):
        positions[num] = i
    
    rounds_needed = [0] * (n + 1)
    
    for num in range(1, n + 1):
        if num == 1:
            rounds_needed[num] = 1
        else:
            if positions[num] > positions[num - 1]:
                rounds_needed[num] = rounds_needed[num - 1]
            else:
                rounds_needed[num] = rounds_needed[num - 1] + 1
    
    return rounds_needed[n]

if __name__ == "__main__":
    print(count_rounds([1, 2, 3, 4])) # 1
    print(count_rounds([1, 3, 2, 4])) # 2
    print(count_rounds([4, 3, 2, 1])) # 4
    print(count_rounds([1])) # 1
    print(count_rounds([2, 1, 4, 7, 5, 3, 6, 8])) # 4

    n = 10**5
    numbers = list(reversed(range(1, n+1)))
    print(count_rounds(numbers)) # 100000