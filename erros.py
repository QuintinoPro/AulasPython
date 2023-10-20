

try:
    letras = ['a','b','c']
    print(letras[2])
except IndexError:
    print("Index não existe")

try:
    valor = int(input("Digite um valor para o Produto: "))
    print(valor)
except:
    print('Digite Numeros')
finally:
    print('Codigo OK')

#else:
 #   print("Foi digitado um valor correto")
  #  resultado = valor * 2
   # print(resultado)