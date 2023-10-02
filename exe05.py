'''Crie um algoritmo que leia um número e diga
se ele é par ou ímpar'''
cont = "s"
while cont == "s" or cont == "S":
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"{numero} é PAR")
    else:
        print(f"{numero} é ÍMPAR")
    cont = input("Deseja continuar? [S/N] ")
else:
    print("Programa encerrado")
