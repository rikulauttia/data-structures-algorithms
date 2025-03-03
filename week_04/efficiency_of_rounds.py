import random
import time

# Listatoteutus
def count_rounds_list(numbers):
    n = len(numbers)
    
    rounds = 1
    for i in range(1, n):
        if numbers.index(i + 1) < numbers.index(i):
            rounds += 1
    
    return rounds

# Sanakirjatoteutus
def count_rounds_dict(numbers):
    n = len(numbers)
    
    pos = {}
    for i, x in enumerate(numbers):
        pos[x] = i
    
    rounds = 1
    for i in range(1, n):
        if pos[i + 1] < pos[i]:
            rounds += 1
    
    return rounds

# Luodaan testidataa
n = 10**7
print(f"Luodaan testidataa koolla {n}...")
numbers = list(range(1, n+1))
random.shuffle(numbers)
print("Testidata luotu")

# Kokeillaan ensin sanakirjatoteutusta
print("Ajetaan sanakirjatoteutus...")
start_time = time.time()
result_dict = count_rounds_dict(numbers)
dict_time = time.time() - start_time
print(f"Sanakirjatoteutuksen tulos: {result_dict}")
print(f"Sanakirjatoteutuksen suoritusaika: {dict_time:.6f} s")

# Listatoteutus on liian hidas ajettavaksi koko datalla (aikavaativuus on O(n²))
# Arvioidaan sen suoritusaika pienemmällä datakoolla
small_n = 10**4
print(f"Luodaan pienempää testidataa koolla {small_n} listatoteutukselle...")
small_numbers = list(range(1, small_n+1))
random.shuffle(small_numbers)

print("Ajetaan listatoteutus pienemmällä datalla...")
start_time = time.time()
result_list = count_rounds_list(small_numbers)
list_time = time.time() - start_time
print(f"Listatoteutuksen tulos pienellä datalla (n={small_n}): {result_list}")
print(f"Listatoteutuksen suoritusaika (n={small_n}): {list_time:.6f} s")

# Ekstrapoloidaan listatoteutuksen suoritusaika alkuperäiselle datakoolle
# O(n²) → jos 10^4 kestää list_time, niin 10^7 kestäisi noin list_time * (10^7/10^4)²
extrapolated_time = list_time * (n/small_n)**2
print(f"Arvioitu listatoteutuksen suoritusaika koolla {n}: {extrapolated_time:.1f} s = {extrapolated_time/3600:.1f} tuntia")

print("\n--- YHTEENVETO ---")
print(f"Listatoteutuksen suoritusaika (arvioitu): {extrapolated_time:.1f} s")
print(f"Sanakirjatoteutuksen suoritusaika: {dict_time:.6f} s")
print(f"Sanakirjatoteutus on noin {extrapolated_time/dict_time:.0f} kertaa nopeampi!")