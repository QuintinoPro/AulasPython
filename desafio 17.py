import math

cat_op = float(input('Cateto Oposto: '))
cat_ad = float(input('Cateto Adjacente: '))

hipo = math.sqrt(cat_op**2 + cat_ad**2)

print(f'\nHipotenusa: {hipo}')