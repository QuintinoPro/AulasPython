
frase = str(input('Digite uma Frase de no Minimo 3 Palavras: ')).strip()
frasemin = frase.lower()

print(f'A sua frase tem {frasemin.count("a")} Letras A')

if frasemin.count('a') > 0:
    print(f'A Primeira Aparição Está localizado na Posição: {frasemin.find("a")+1}')
    print(f'A Ultima Aparição Está localizado na Posição: {frasemin.rfind("a")+1}')
else:
    print("A letra A não aparece")