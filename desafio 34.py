
sal = float(input('Digite seu Salario: '))

if sal > 1250:
    aumento = sal * 0.1
    newsal = aumento + sal
    print('Aumento de 10%')
    print(f'Aumento: {aumento}')
    print(f'Novo Salario: {newsal}')
elif sal <= 1250:
    aumento = sal * 0.15
    newsal = aumento + sal
    print('Aumento de 15%')
    print(f'Aumento: {aumento}')
    print(f'Novo Salario: {newsal}')