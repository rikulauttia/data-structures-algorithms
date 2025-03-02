def check_year(year):
    left_part = year // 100
    right_part = year % 100
    return (left_part + right_part) ** 2 == year

if __name__ == "__main__":
    print(check_year(1995)) # False
    print(check_year(2024)) # False
    print(check_year(2025)) # True
    print(check_year(2026)) # False
    print(check_year(3025)) # True
    print(check_year(5555)) # False