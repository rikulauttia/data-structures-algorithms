def count_steps(numbers):
    if not numbers:
        return 0
    
    indexed_numbers = [(num, idx) for idx, num in enumerate(numbers)]
    
    indexed_numbers.sort()
    
    # Robotti aloittaa kohdasta 0
    current_position = 0
    total_steps = 0
    
    for _, idx in indexed_numbers:
        steps = abs(idx - current_position)
        total_steps += steps
        
        current_position = idx
    
    return total_steps

if __name__ == "__main__":
    print(count_steps([1])) # 0
    print(count_steps([1, 2, 3])) # 2
    print(count_steps([3, 2, 1])) # 4
    print(count_steps([42, 1337, 1, 10**9])) # 7
    print(count_steps([1, 3, 5, 7, 8, 6, 4, 2])) # 28
    print(count_steps([10**6, 10**8, 10**7, 10**9])) # 5

    numbers = [(x * 999983) % 10**9 + 1 for x in range(10**5)]
    print(count_steps(numbers)) # 4871908997