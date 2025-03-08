def count_pairs(numbers):
    # Tehdään kopio listasta, jotta alkuperäinen ei muutu
    sorted_numbers = sorted(numbers)
    
    n = len(sorted_numbers)
    count = 0
    used = [False] * n  # Pitää kirjaa jo käytetyistä luvuista
    
    # Käydään läpi pienemmät luvut järjestyksessä
    for i in range(n):
        if used[i]:
            continue  # Ohitetaan jo käytetyt luvut
            
        # Etsitään pienin kelvollinen pari
        for j in range(n):
            if not used[j] and j != i and sorted_numbers[j] >= 2 * sorted_numbers[i]:
                # Löytyi pari
                used[i] = True
                used[j] = True
                count += 1
                break  # Siirrytään seuraavaan pienempään lukuun
    
    return count

if __name__ == "__main__":
    print(count_pairs([1])) # 0
    print(count_pairs([1, 2, 3])) # 1
    print(count_pairs([1, 2, 3, 4])) # 2
    print(count_pairs([1, 1, 1, 1])) # 0
    print(count_pairs([10**9, 1, 1, 1])) # 1
    print(count_pairs([4, 5, 1, 4, 7, 8])) # 2
    print(count_pairs([1, 2, 3, 2, 4, 6])) # 3

    numbers = [(x * 999983) % 10**6 + 1 for x in range(10**5)]
    print(count_pairs(numbers)) # 41176