from sys import getsizeof


numeros = [x * 10 for x in range(77777777)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

numeros = (x * 10 for x in range(77777777))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))