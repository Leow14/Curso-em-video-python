sal = str(input('Qual é o salário do funcionário? R$').strip())
sa = float(sal)
if sa <= 1250.00:
    sb = ((15*sa)/100)+sa
    print(f'Seu novo salário é {sb}')
else:
    sh = ((10*sa)/100)+sa
    print(f'Seu novo sálario é {sh}')
