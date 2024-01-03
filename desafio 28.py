import random

numero = random.randint(0,5)

while True:
    num_usu = int(input('Digite um Numero entre 0 - 5: '))

    if num_usu == numero:
        print(f'Voce acertou o numero que o PC escolheu!')
        break
    else:
        print(f'Tente novamente!')

