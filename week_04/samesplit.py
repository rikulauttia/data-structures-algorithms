def count_splits(numbers):
    total_counts = {}
    for num in numbers:
        total_counts[num] = total_counts.get(num, 0) + 1
    
    for count in total_counts.values():
        if count < 2:
            return 0
    
    # Kaikki uniikit numerot
    unique_nums = list(total_counts.keys())
    unique_count = len(unique_nums)
    
    valid_splits = 0
    left_counts = {num: 0 for num in unique_nums}
    
    # Seurantamuuttujat
    left_present = set()
    right_missing = set(unique_nums)
    
    for i in range(len(numbers) - 1):
        num = numbers[i]
        
        left_counts[num] += 1
        
        if num not in left_present:
            left_present.add(num)
        
        if total_counts[num] - left_counts[num] == 0:
            right_missing.add(num)
        elif num in right_missing:
            right_missing.remove(num)
        
        if len(left_present) == unique_count and len(right_missing) == 0:
            valid_splits += 1
    
    return valid_splits

if __name__ == "__main__":
    print(count_splits([1, 1, 1, 1])) # 3
    print(count_splits([1, 1, 2, 1])) # 0
    print(count_splits([1, 2, 1, 2])) # 1
    print(count_splits([1, 2, 3, 4])) # 0
    print(count_splits([1, 2, 1, 2, 1, 2])) # 3

    numbers = [1, 2] * 10**5
    print(count_splits(numbers)) # 199997
    numbers = list(range(1, 10**5 + 1)) * 2
    print(count_splits(numbers)) # 1