
numeros = []

for i in range(3):
    numero = int(input(f'Digite o {i+1}º Numero:'))
    numeros.append(numero)

numeros.sort() #Ordem Crescente

menor = numeros[0]
maior = numeros[-1]


print(f'{menor} é o menor número!')
print(f'{maior} é o maior número!')
