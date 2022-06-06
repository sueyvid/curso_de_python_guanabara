'''from random import sample
alunos = 4
aluno1 = input('Digite o nome do primeiro aluno: ')
aluno2 = input('Digite o nome do segundo aluno: ')
aluno3 = input('Digite o nome do terceiro aluno: ')
aluno4 = input('Digite o nome do quarto aluno: ')
l = [aluno1, aluno2, aluno3, aluno4]
print('A ordem de apresentação será: \n{}'.format(sample(l, alunos)))'''

from random import shuffle
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
l = [n1, n2, n3, n4]
shuffle(l)
print('A ordem de apresentação será: \n{}'.format(l))
