def find_distances(street):
    n = len(street)
    distances = [0] * n
    
    for i in range(n):
        if street[i] == '0':
            distances[i] = n + 1

    # Käydään merkkijono läpi vasemmalta oikealle
    last_shop = -1
    for i in range(n):
        if street[i] == '1':
            last_shop = i
        if last_shop != -1:
            distances[i] = min(distances[i], i - last_shop)
    
    # Käydään merkkijono läpi oikealta vasemmalle
    last_shop = -1
    for i in range(n-1, -1, -1):
        if street[i] == '1':
            last_shop = i
        if last_shop != -1:
            distances[i] = min(distances[i], last_shop - i)

    return distances

if __name__ == "__main__":
    print(find_distances("00100010")) # [2, 1, 0, 1, 2, 1, 0, 1]
    print(find_distances("00100000")) # [2, 1, 0, 1, 2, 3, 4, 5]
    print(find_distances("11111111")) # [0, 0, 0, 0, 0, 0, 0, 0]
    print(find_distances("01010101")) # [1, 0, 1, 0, 1, 0, 1, 0]
    print(find_distances("10000000")) # [0, 1, 2, 3, 4, 5, 6, 7]
    print(find_distances("00000001")) # [7, 6, 5, 4, 3, 2, 1, 0]

    n = 10**5
    street = "0"*n + "1" + "0"*n
    distances = find_distances(street)
    print(distances[1337]) # 98663