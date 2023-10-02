soma = 0
for x in range(1,5):
    numero = int(input(f"Digite o {x}º número: "))
    soma += numero
media = soma / 4
print(f"A soma dos valores é: {soma}. E a média é: {media}")
