valores = tuple(int(input("Digite um valor: ")) for _ in range(4))

contador_9 = valores.count(9)

posicao_3 = valores.index(3) + 1 if 3 in valores else 0


pares = tuple(num for num in valores if num % 2 == 0)

print(f"O valor 9 apareceu {contador_9} vezes.")
print(f"A primeira ocorrência do valor 3 foi na posição {posicao_3}.")
print(f"Os números pares são: {pares}")
