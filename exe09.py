cont = "s"
while cont == "s" or cont == "S":
    print(">>> Digite um número para saber seu ANTECESSOR ou SUCESSOR <<<"'''
    [1] Antecessor
    [2] Sucessor
    [3] Encerrar''')
    menu = int(input("Escolha um número: "))
    if menu == 1:
        numero = int(input("Digite um número: "))
        antecessor = numero - 1
        print(f"O antecessor de {numero} é: {antecessor}")
    elif menu == 2:
        numero = int(input("Digite um número: "))
        sucessor = numero + 1
        print(f"O sucessor de {numero} é: {sucessor}")
    else:
        print("Número inválido.")
    cont = input("Deseja continuar? [S/N] ")
else:
    print("Programa encerrado")
