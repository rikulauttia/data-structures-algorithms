import time

n = 10**5

lista = []

alku_aika_lisays = time.time()

for i in range(1, n+1):
    lista.append(i)

loppu_aika_lisays = time.time()
lisays_aika = loppu_aika_lisays - alku_aika_lisays

alku_aika_poisto = time.time()

for i in range(n):
    lista.pop()

loppu_aika_poisto = time.time()
poisto_aika = loppu_aika_poisto - alku_aika_poisto

print(f"Lisäämisen kesto: {lisays_aika:.6f} s")
print(f"Poistamisen kesto: {poisto_aika:.6f} s")