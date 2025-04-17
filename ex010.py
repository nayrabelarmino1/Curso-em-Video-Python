#Crie um programa que leia quanto dinheiro uma pessoa tem a carteira e mostre quantos Dólares ela pode comprar.
#A cotação do dólar no dia em que fiz o exercício era de R$5.28

real = float(input('Quanto de dinheiro você tem na carteira? R$ '))
dolar = real / 5.28
euro = real / 5.37
print('Com R${:.2f} você pode comprar US${:.2f} ou €{:.2f}'.format(real, dolar, euro))
