import time
import random

def count_even_1(numbers):
    result = 0
    for x in numbers:
        if x % 2 == 0:
            result += 1
    return result

def count_even_2(numbers):
    return sum(x % 2 == 0 for x in numbers)

if __name__ == "__main__":
    numbers = [random.randint(1, 100) for _ in range(10**7)]
    
    # toteutus1
    start_time = time.time()
    result1 = count_even_1(numbers)
    end_time = time.time()
    toteutus1_time = end_time - start_time
    
    # toteutus2
    start_time = time.time()
    result2 = count_even_2(numbers)
    end_time = time.time()
    toteutus2_time = end_time - start_time
    
    print(f"Toteutuksen 1 suoritusaika: {toteutus1_time:.6f} s")
    print(f"Toteutuksen 2 suoritusaika: {toteutus2_time:.6f} s")
    print(f"Tulokset: {result1}, {result2}")
