'''Ler um valor e escrever a mensagem É MAIOR
QUE 10! se o valor lido for maior que 10, caso
contrário escrever NÃO É MAIOR QUE 10!'''
numer = int(input("Digite um número: "))
if numer == 10:
    print(f"{numer} é igual a 10")
elif numer > 10:
    print(f"{numer} é maior que 10")
else:
    print(f"{numer} é menor que 10")