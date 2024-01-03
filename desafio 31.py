
kmviagem = int(input("Digite a KM da sua Viagem: "))

if kmviagem <= 200:
    passagem = 0.5 * kmviagem
    print(f'Sua viagem vai custar: R${passagem}')
else:
    passagem = 0.45 * kmviagem
    print(f'Sua viagem vai custar: R${passagem}')
