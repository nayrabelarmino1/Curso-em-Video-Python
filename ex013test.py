produto = float(input('Qual é o preço do produto? R$ '))
avista = produto - (produto * 10 / 100)
parcelado = produto + (produto * 5 / 100)
print('O preço do produto é R${:.2f}, pagando a vista receberá 10% de desconto totalizando R${:.2f}.\n '
      'E parcelado receberá um juros de 5% no valor ficando R${:.2f}.'.format(produto, avista, parcelado))

