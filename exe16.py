valor = 0

quantidadeMacas = int(input("Digite quantidade de maças: "))

if quantidadeMacas > 12:
    valor = 1.0
else:
    valor = 1.30
custo = valor * quantidadeMacas

print(f"O custo de maças compradas foi: {custo}")