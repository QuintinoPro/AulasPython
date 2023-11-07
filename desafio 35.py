
retas = []

for i in range(3):
    reta = float(input(f'Digite o tamanho da {i+1}º Reta:'))
    retas.append(reta)

if retas[0] < retas[1] + retas[2] and retas[1] < retas[0] + retas[2] and retas[2] < retas[0] + retas[1]:
    print('Podemos formar triangulo!')
else:
    print('Não forma um triangulo!')