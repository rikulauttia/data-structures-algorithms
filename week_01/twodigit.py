from itertools import product

def count_numbers(a, b):
    valid_digits = {'2', '5'}
    
    def generate_valid_numbers(limit):
        valid_numbers = set()
        for length in range(1, len(str(limit)) + 1):
            for num_tuple in product(valid_digits, repeat=length):
                num = int("".join(num_tuple))
                if num > limit:
                    break
                valid_numbers.add(num)
        return sorted(valid_numbers)
    
    valid_numbers = generate_valid_numbers(b)
    return sum(1 for num in valid_numbers if a <= num <= b)


if __name__ == "__main__":
    print(count_numbers(1, 100)) # 6
    print(count_numbers(60, 70)) # 0
    print(count_numbers(25, 25)) # 1
    print(count_numbers(1, 10**9)) # 1022
    print(count_numbers(123456789, 987654321)) # 512