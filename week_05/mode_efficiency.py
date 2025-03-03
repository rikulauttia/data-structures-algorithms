import random
import time

def create_data(n, alaraja, ylaraja):
    return [random.randint(alaraja, ylaraja) for _ in range(n)]

# Sanakirjaa käyttävä toteutus
def find_mode_dict(numbers):
    count = {}
    mode = numbers[0]

    for x in numbers:
        if x not in count:
            count[x] = 0
        count[x] += 1

        if count[x] > count[mode]:
            mode = x

    return mode

# Järjestämistä käyttävä toteutus
def find_mode_sort(numbers):
    numbers.sort()
    
    current_number = numbers[0]
    current_count = 1
    max_count = 1
    mode = current_number
    
    for i in range(1, len(numbers)):
        if numbers[i] == current_number:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                mode = current_number
            current_number = numbers[i]
            current_count = 1
    
    if current_count > max_count:
        mode = current_number
    
    return mode

def suorita_testi():
    n = 10**7
    alaraja = 1
    ylaraja = 1000
    
    print(f"Luodaan {n} satunnaista lukua väliltä {alaraja}-{ylaraja}...")
    luvut = create_data(n, alaraja, ylaraja)
    luvut_kopio = luvut.copy()
    
    # Testataan sanakirjatoteutus
    print("Testataan sanakirjatoteutusta...")
    alku = time.time()
    moodi_dict = find_mode_dict(luvut)
    loppu = time.time()
    aika_dict = loppu - alku
    
    # Testataan järjestämistoteutus
    print("Testataan järjestämistoteutusta...")
    alku = time.time()
    moodi_sort = find_mode_sort(luvut_kopio)
    loppu = time.time()
    aika_sort = loppu - alku

    print(f"\nSanakirjatoteutuksen löytämä moodi: {moodi_dict}")
    print(f"Järjestämistoteutuksen löytämä moodi: {moodi_sort}")
    print(f"\nSanakirjatoteutuksen suoritusaika: {aika_dict:.6f} s")
    print(f"Järjestämistoteutuksen suoritusaika: {aika_sort:.6f} s")
    
    return aika_dict, aika_sort

if __name__ == "__main__":
    aika_dict, aika_sort = suorita_testi()