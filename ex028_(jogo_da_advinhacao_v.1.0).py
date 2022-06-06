from random import randint
escolha = randint(0, 5)
print('O computador pensou em um número.')
num = int(input('Qual foi o número escolhido pelo computador? (entre 0 e 5): '))
print('ACERTOU!!!' if escolha == num else 'ERROU!')
print('O número era {}'.format(escolha))