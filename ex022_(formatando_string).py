nome = input('Digite seu nome completo: ')
print('- Nome com todas as letras maiúsculas: \n{}'.format(nome.upper()))
print('- Nome com todas as letras minúsculas: \n{}'.format(nome.lower()))

espacos = nome.count(' ')
tamanho = len(nome) - espacos
print('- Quantidade de letras (sem considerar espaços): \n{}'.format(tamanho))

letras = nome.split()
print('- Quantidade de letras do primeiro nome: \n{}'.format(len(letras[0])))
