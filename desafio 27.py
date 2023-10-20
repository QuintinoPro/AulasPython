
nome = str(input("Digite seu Nome Completo: "))

nomesepa = nome.split()

print(f'Primeiro Nome: {nomesepa[0]}')
print(f'Ultimo Nome: {nomesepa[len(nomesepa)-1]}')