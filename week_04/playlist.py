def count_parts(songs):
    n = len(songs)
    result = 0
    left = 0
    song_counts = {}
    
    for right in range(n):
        if songs[right] in song_counts:
            song_counts[songs[right]] += 1
        else:
            song_counts[songs[right]] = 1
        
        # Jos nykyinen biisi esiintyy useammin kuin kerran, kavennetaan ikkunaa vasemmalta kunnes nykyistä biisiä on vain yksi kappale
        while song_counts[songs[right]] > 1:
            song_counts[songs[left]] -= 1
            if song_counts[songs[left]] == 0:
                del song_counts[songs[left]]
            left += 1
        
        # Lisätään tulos: kaikki tämänhetkiseen (right) loppuvat kelvolliset osalistat
        result += right - left + 1
    
    return result

if __name__ == "__main__":
    print(count_parts([1, 1, 1, 1])) # 4
    print(count_parts([1, 2, 3, 4])) # 10
    print(count_parts([1, 2, 1, 2])) # 7
    print(count_parts([1, 2, 1, 3])) # 8
    print(count_parts([1, 1, 2, 1])) # 6

    songs = [1, 2] * 10**5
    print(count_parts(songs)) # 399999
    songs = list(range(1, 10**5 + 1)) * 2
    print(count_parts(songs)) # 15000050000