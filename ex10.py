'''Faça um algoritmo que leia a idade de
uma pessoa expressa em anos, meses e dias
e escreva a idade dessa pessoa expressa
apenas em dias. Considerar ano com 365
dias e mês com 30 dias'''
idade = int(input("Digite sua idade: "))
mes = int(input("Digite o mês atural: "))
dia = int(input("Digite o dia atual: "))
idade_em_dias = (idade * 365) + (mes * 30) + dia
print("A idade em dias é:", idade_em_dias)
