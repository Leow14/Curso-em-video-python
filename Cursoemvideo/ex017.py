ca = float(input('Informe o valor do cateto adjacente:'))
co = float(input('Informe o valor do cateto oposto:'))
hip = ca**2 + co**2
hipr = hip**(1/2)
print('A hipotenusa do triângulo irá medir {:.4}'.format(hipr))