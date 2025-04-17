#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-=-' * 10)
print('\033[4;35mAnalisador de Triângulos\033[m')
print('-=-' * 10)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima \033[2;32mPODEM\033[m formar um triângulo.')
else:
    print('Os segmentos acima \033[2;31mNÃO PODEM\033[m formar um triângulo.')
