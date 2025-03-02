def find_sums(numbers, size):
    n = len(numbers)
    
    # Jos osalistan koko on suurempi kuin listan pituus, ei voida muodostaa osalistoja.
    if size > n:
        return []
    
    # Osalistojen määrä
    result_length = n - size + 1
    
    # Luodaan tulos-lista
    sums = [0] * result_length
    
    # Lasketaan ensimmäisen osalistan summa
    first_sum = sum(numbers[:size])
    sums[0] = first_sum
    
    # Lasketaan muiden osalistojen summat hyödyntäen edellistä summaa
    for i in range(1, result_length):
        # Uusi summa = edellinen summa - poistuva luku  + uusi luku
        sums[i] = sums[i-1] - numbers[i-1] + numbers[i+size-1]
    
    return sums

if __name__ == "__main__":
    print(find_sums([1], 1)) # [1]
    print(find_sums([1, 8, 2, 7, 3, 6, 4, 5], 6)) # [27, 30, 27]

    print(find_sums([1, 2, 3, 4, 5], 1)) # [1, 2, 3, 4, 5]
    print(find_sums([1, 2, 3, 4, 5], 2)) # [3, 5, 7, 9]
    print(find_sums([1, 2, 3, 4, 5], 3)) # [6, 9, 12]
    print(find_sums([1, 2, 3, 4, 5], 4)) # [10, 14]
    print(find_sums([1, 2, 3, 4, 5], 5)) # [15]

    numbers = list(range(10**5))
    sums = find_sums(numbers, 10**4)
    print(sums[5]) # 50045000
    print(sums[42]) # 50415000
    print(sums[1337]) # 63365000