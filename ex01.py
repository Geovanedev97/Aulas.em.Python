'''1. Faça um algoritmo que receba 2
notas e calcule a média aritmética'''
refazer = "s"
while refazer == "s" or refazer == "S":
    num1 = float(input("Digite a primeira nota: "))
    while num1 < 0 or num1 > 10:
        num1 = float(input("Nota inválida. Digite novamente: "))
    num2 = float(input("Digite a segunda nota: "))
    while num2 < 0 or num2 > 10:
        num2 = float(input("Nota inválida. Digite novamente: "))
    media = (num1 + num2) / 2
    print(f"A média das notas é: {media}")
    refazer = input("Deseja refazer? [S/N] ")
else:
    print("Programa encerrado")
