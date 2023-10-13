import math
import random

alunos = ['Joao', 'Luiz', 'Cleiton', 'James']

random.shuffle(alunos)

print("\nOrdem de Apresentação:")
for x, aluno in enumerate(alunos, start=1):
    print(f'{x}. {aluno}')
