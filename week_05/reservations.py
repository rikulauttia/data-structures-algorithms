import random

def check_overlapping(reservations):
    # Jos varauksia on vähemmän kuin 2, ei voi olla päällekkäisyyksiä
    if len(reservations) < 2:
        return False
    
    # Järjestetään varaukset alkupäivän mukaan
    sorted_reservations = sorted(reservations)
    
    # Käydään läpi järjestetyt varaukset
    for i in range(len(sorted_reservations)-1):
        current_start, current_end = sorted_reservations[i]
        next_start, next_end = sorted_reservations[i+1]
        
        # Jos nykyisen varauksen loppupäivä on suurempi tai yhtä suuri kuin
        # seuraavan varauksen alkupäivä, varaukset menevät päällekkäin
        if current_end >= next_start:
            return True
    
    return False

if __name__ == "__main__":
    print(check_overlapping([])) # False
    print(check_overlapping([(1, 3)])) # False
    print(check_overlapping([(4, 7), (1, 2)])) # False
    print(check_overlapping([(4, 7), (1, 5)])) # True
    print(check_overlapping([(1, 1), (2, 2)])) # False
    print(check_overlapping([(1, 1), (1, 1)])) # True
    print(check_overlapping([(2, 3), (5, 5), (3, 4)])) # True
    print(check_overlapping([(2, 3), (5, 5), (1, 4)])) # True
    print(check_overlapping([(2, 3), (5, 5), (1, 5)])) # True

    reservations = [(day, day) for day in range(1, 10**5+1)]
    random.shuffle(reservations)
    print(check_overlapping(reservations)) # False

    reservations.append((42, 1337))
    random.shuffle(reservations)
    print(check_overlapping(reservations)) # True