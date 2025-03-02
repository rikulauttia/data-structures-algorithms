def find_rounds(numbers):
    remaining = numbers.copy()
    
    rounds = []
    
    while remaining:
        current_round = []
        
        i = 0
        next_number = min(remaining)
        
        while i < len(remaining):
            if remaining[i] == next_number:
                current_round.append(next_number)
                remaining.pop(i)
                next_number += 1
            else:
                i += 1
        
        rounds.append(current_round)
    
    return rounds

if __name__ == "__main__":
    print(find_rounds([1, 2, 3, 4]))
    # [[1, 2, 3, 4]]

    print(find_rounds([1, 3, 2, 4]))
    # [[1, 2], [3, 4]]    

    print(find_rounds([4, 3, 2, 1]))
    # [[1], [2], [3], [4]]
    
    print(find_rounds([1]))
    # [[1]]

    print(find_rounds([2, 1, 4, 7, 5, 3, 6, 8]))
    # [[1], [2, 3], [4, 5, 6], [7, 8]]