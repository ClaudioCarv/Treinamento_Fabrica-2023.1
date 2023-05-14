valores = []
for i in range(5):
    valor = int(input("Digite um valor: "))
    if i == 0 or valor >= valores[-1]:
        valores.append(valor)
    else:
        for j in range(len(valores)):
            if valor <= valores[j]:
                valores.insert(j, valor)
                break

print("Valores ordenados:", valores)
