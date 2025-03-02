def check_number(number):
    if len(number) != 9 or number[0] != '0' or not number.isdigit():
        return False
    
    weights = [3, 7, 1, 3, 7, 1, 3, 7]
    sum_value = sum(int(number[i]) * weights[i] for i in range(8))
    
    check_digit = (10 - (sum_value % 10)) % 10
    
    return check_digit == int(number[-1])

if __name__ == "__main__":
    print(check_number("012749138")) # False
    print(check_number("012749139")) # True
    print(check_number("013333337")) # True
    print(check_number("012345678")) # False
    print(check_number("012344550")) # True
    print(check_number("1337")) # False
    print(check_number("0127491390")) # False