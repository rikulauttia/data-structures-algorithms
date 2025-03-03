def count_splits(sequence):
    count = 0
    
    total_zeros = sequence.count('0')
    total_ones = sequence.count('1')
    
    left_zeros = 0
    left_ones = 0
    
    for i in range(len(sequence) - 1):
        if sequence[i] == '0':
            left_zeros += 1
        else:
            left_ones += 1
        
        right_zeros = total_zeros - left_zeros
        right_ones = total_ones - left_ones
        
        if left_zeros == left_ones and right_zeros == right_ones:
            count += 1
    
    return count

if __name__ == "__main__":
    print(count_splits("00")) # 0
    print(count_splits("01")) # 0
    print(count_splits("0110")) # 1
    print(count_splits("010101")) # 2
    print(count_splits("000111")) # 0
    print(count_splits("01100110")) # 3

    sequence = "01"*10**5
    print(count_splits(sequence)) # 99999