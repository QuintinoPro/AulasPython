
num = int(input('Digite um numero de 0 a 9999: '))

if 0 <= num <= 9999:
    unidade = num % 10
    num //= 10  # Remove a unidade
    dezena = num % 10
    num //= 10  # Remove a dezena
    centena = num % 10
    num //= 10  # Remove a centena
    milhar = num  # O que sobrar será a milhar

    print(f'Milhar: {milhar}')
    print(f'Centena: {centena}')
    print(f'Dezena: {dezena}')
    print(f'Unidade: {unidade}')
else:
    print('Número fora do intervalo válido (0 a 9999).')