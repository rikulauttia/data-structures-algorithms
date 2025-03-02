def count_sublists(numbers):
    result = 0
    
    even_count = 0
    
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
            result += even_count
        else:
            even_count = 0

    return result

if __name__ == "__main__":
    print(count_sublists([2, 4, 1, 6])) # 4
    print(count_sublists([1, 2, 3, 4])) # 2
    print(count_sublists([1, 1, 1, 1])) # 0
    print(count_sublists([2, 2, 2, 2])) # 10
    print(count_sublists([1, 1, 2, 1])) # 1

    numbers = [2] * 10**5
    print(count_sublists(numbers)) # 5000050000