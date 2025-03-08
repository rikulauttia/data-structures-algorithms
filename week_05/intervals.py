import random

def count_nested(intervals):
    if not intervals:
        return 0
    
    # Järjestelmällisempi lähestymistapa:
    # 1. Järjestä kaikki lukuvälit alku- ja loppupisteiden mukaan
    # 2. Käy läpi lukuvälit tehokkaasti
    
    # Lukuvälien määrä, jotka ovat jonkin toisen lukuvälin sisällä
    count = 0
    
    # Erotetaan alku- ja loppupisteet ja merkitään, mihin lukuväliin ne kuuluvat
    points = []
    for i, (start, end) in enumerate(intervals):
        # Lisätään alkupiste (arvo, tyyppi, lukuvälin indeksi)
        # Tyyppi 0 = alkupiste, 1 = loppupiste
        points.append((start, 0, i))
        points.append((end, 1, i))
    
    # Järjestetään pisteet arvojen mukaan
    # Jos arvot ovat samat, loppupisteet tulevat ensin
    points.sort(key=lambda x: (x[0], x[1]))
    
    # Käytä setti-tietorakennetta avoimien lukuvälien seuraamiseen
    open_intervals = set()
    # Seuraa, montako lukuväliä on jokaisen lukuvälin sisällä
    contained_in = [0] * len(intervals)
    
    for point, point_type, interval_idx in points:
        if point_type == 0:  # Alkupiste
            # Lisätään lukuvälin indeksi avoimiin lukuväleihin
            contained_in[interval_idx] = len(open_intervals)
            open_intervals.add(interval_idx)
        else:  # Loppupiste
            # Poistetaan lukuvälin indeksi avoimista lukuväleistä
            open_intervals.remove(interval_idx)
    
    # Laske, montako lukuväliä on ainakin yhden toisen lukuvälin sisällä
    for value in contained_in:
        if value > 0:
            count += 1
    
    return count

if __name__ == "__main__":
    print(count_nested([])) # 0
    print(count_nested([(1, 2)])) # 0
    print(count_nested([(1, 2), (3, 4)])) # 0
    print(count_nested([(1, 3), (2, 4)])) # 0
    print(count_nested([(1, 4), (2, 3)])) # 1
    print(count_nested([(1, 4), (1, 3)])) # 1
    print(count_nested([(1, 4), (2, 4)])) # 1
    print(count_nested([(1, 1), (1, 2), (1, 3)])) # 2
    print(count_nested([(1, 6), (2, 5), (3, 4)])) # 2
    print(count_nested([(1, 4), (2, 5), (3, 6)])) # 0

    intervals = [(x+1, x+3) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 0

    intervals = [(x+1, 2*10**5-x) for x in range(10**5)]
    random.shuffle(intervals)
    print(count_nested(intervals)) # 99999