#aula de dicionario

carros = {"Jeep Renegade": {"Preço": "R$ 90.000,00", "Ano": 2023},
          "Jeep Compass": 'R$ 150.000,00',
          "Troller": 'R$ 200.000,00'}

print("Jeep Renegade","\nAno",carros["Jeep Renegade"]["Ano"],"\nPreço", carros["Jeep Renegade"]["Preço"])

del carros["Troller"]

carros["Audi"] = [2023]

carros["Jeep Renegade"]["Preço"] = "R$ 100.000,00"
print(carros.values())

print(carros)


estoque = {"mouse": 15,"teclado": 25,"headset": 50,"monitor": 500}
while True:
    produto = input("Digite o nome do produto ou fim para finalizar: ")
    if produto=="fim":
        break
    if produto in estoque:
        print(f"Preço R$ {estoque[produto]:.2f}")
    else:
        print("Produto não encontrado.")

