#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é \033[4;35m{}\033[m.'.format(nome[0]))
print('E seu último nome é \033[4;34m{}\033[m.'.format(nome[len(nome)-1]))
