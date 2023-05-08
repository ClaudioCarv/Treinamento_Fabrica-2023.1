while True:
    num = int(input("Digite um número (negativo para sair): "))
    if num < 0:
        break
    print(f"Tabuada do {num}:")
    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
