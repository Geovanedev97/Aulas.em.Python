total = int(input("Digite o total de eleitores: "))
brancos = int(input("Digite o total de votos brancos: "))
nulos = int(input("Digite o total de votos nulos: "))
validos = int(input("Digite o total de votos válidos: "))
percentual_brancos = (100 * brancos) / total
percentual_nulos = (100 * nulos) / total
percentual_validos = (100 * validos) / total
print(f"O percetual de votos brancos foi: {percentual_brancos:.2f}%")
print(f"O percentual de votos nulos foi: {percentual_nulos:.2f}%")
print(f"O percentual de votos validos foi:{percentual_validos:.2f}%")
