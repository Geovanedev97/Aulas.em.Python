'''Crie um algoritmo que leia um número
diferente de zero e diga se este número é
positivo ou negativo'''
refazer = "s"
while refazer == "s" or refazer == "S":
    numero = int(input("Digite um número para saber se é POSITIVO ou NEGATIVO: "))
    while numero == 0:
        numero = int(input("Digite um número diferente de 0: "))
    if numero < 0:
        print(f"{numero} é NEGATIVO")
    else:
        print(f"{numero} é POSITIVO")
    refazer = input("Deseja continuar? [S/N] ")
else:
    print("Programa encerrado")