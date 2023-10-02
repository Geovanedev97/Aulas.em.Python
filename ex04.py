'''Crie um algoritmo que receba 3 números e
informe qual o maior entre eles.'''
refazer = "s"
while refazer == "s" or refazer == "S":
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    num3 = int(input("Digite o terceiro número: "))
    if num1 > num2:
        if num1 > num3:
            print(f"{num1} é maior número")
        else:
            print(f"{num3} é o maior")
    elif num2 > num3:
        print(f"{num2} é o maior")
    else:
        print(f"{num3} é o maior")
    refazer = input("Deseja continuar? [S/N] ")
else:
    print("Programa encerrado.")
