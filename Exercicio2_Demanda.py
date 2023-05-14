produtos = ("Produto 1", 10.99, "Produto 2", 15.50, "Produto 3", 20.25)

print("PRODUTOS\t\tPREÇOS")
print("-------------------------")
for i in range(0, len(produtos), 2):
    print(f"{produtos[i]:<15}\tR$ {produtos[i+1]:.2f}")