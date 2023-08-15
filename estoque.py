estoque = {"Snickers": [50, 3],
           "Trento": [40, 2.5],
           "Bis": [60, 7],
           "M&Ms": [30, 5],
           "Milka": [45, 10],
           "Twix": [20, 4]}

total = 0
while True:
    prod = input("Produto: ")
    if prod == "fim":
        break
    if prod in estoque:
        quant = int(input("Quantidade: "))
        if quant <= estoque[prod][0]:
            preco = estoque[prod][1]
            custo = preco * quant
            print(f'{prod}: {quant} X R${preco:.2f} = R${custo:.2f}')
            estoque[prod][0] -= quant
            total += custo
        else:
            print("Quantidade indisponível.")
    else:
        print("Produto indisponível.")

print(f"\nTotal = R${total:.2f}")

for chave, dados in estoque.items():
    print("\nDescrição:",chave)
    print("Quantidade:",dados[0])
    print(f"Preço: R${dados[1]:.2f}")
