
frutas = ['abacate','banana','morango','kiwi','abacaxi']

print(frutas)

frutas1 = []

for x in frutas:
    if 'a' in x:
        frutas1.append(x)

print(frutas1)

frutas2 = [iten for iten in frutas if 'n' in iten]

print(frutas2)

valores = []

for y in range(7):
    valores.append(y*10)

print(valores)

valor = [z * 10 for z in range(7)]

print(valor)