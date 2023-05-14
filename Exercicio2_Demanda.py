import random

numeros = tuple(random.sample(range(1, 101), 5))

print("Números gerados:", numeros)
print("Menor valor:", min(numeros))
print("Maior valor:", max(numeros))
