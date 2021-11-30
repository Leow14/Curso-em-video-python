print('Aluguel de carros Leonardo')
km =float(input('O carro percorreu quantos km?'))
dia =float(input('Quantos dias o carro foi usado?'))
pkm = km * 0.15
pdia = dia * 60
p = pdia + pkm
print(f'O valor a ser pago é de {p}')
