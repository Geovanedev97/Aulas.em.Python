'''Crie um código que leia a idade de
uma pessoa e diga em qual ano ela
nasceu'''
refazer = "s"
while refazer == "s" or refazer == "S":
    idade = int(input("Digite sua idade: "))
    ano = 2023 - idade
    print(f"Você nasceu em: {ano}")
    refazer = input("Deseja continuar? [S/N] ")
else:
    print("Programa encerrado.")
