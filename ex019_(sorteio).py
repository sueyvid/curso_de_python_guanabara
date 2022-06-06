'''from random import randint, sample
alunos = 4
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
l = [aluno1, aluno2, aluno3, aluno4]
i = randint(0, alunos-1)
print(sample(l, 1))'''

'''from random import randint
alunos = 4
aluno1 = input('Nome do primeiro aluno: ')
aluno2 = input('Nome do segundo aluno: ')
aluno3 = input('Nome do terceiro aluno: ')
aluno4 = input('Nome do quarto aluno: ')
l = [aluno1, aluno2, aluno3, aluno4]
print('O aluno(a) escolhido(a) foi: {}'.format(l[randint(0, alunos-1)]))'''

from random import choice
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
l = [n1, n2, n3, n4]
escolhido = choice(l)
print('O escolhido(a) foi: {}'.format(escolhido))
