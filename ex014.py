#Escreva um programa que converta uma temperatura digitada em °C e converta para °F.

C = float(input('Informe a temperatura em °C: '))
F = C * 1.8 + 32
print('A temperatura de {}°C corresponde a {}°F.'.format(C, F))
