
vel = int(input("Digite a Velocidade do seu Carro: "))

if vel > 80:
    print(f'Voce Sera Multado!')
    velmais = vel - 80
    multa = velmais * 7
    print(f'Sua multa é: R${multa}')
else:
    print(f'Velocidade Permitida!')