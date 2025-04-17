#Crie um programa que diga o dobro, o triplo e a raiz quadrada de um valor.

n = int(input('Digite um valor: '))
d = n*2
t = n*3
r = n** (1/2)
print('O dobro de {} é {}.'.format(n, d))
print('O triplo de {} é {}.'.format(n, t))
print('A raiz quadrada de {} é {:.2f}.'.format(n, r))
