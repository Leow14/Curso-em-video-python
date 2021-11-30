divida = float(input())
mensal = float(input())
pagamento = 1
while divida > 0:
    print(f'pagamento: {pagamento:.0f}')
    print(f'antes = {divida:.0f}')
    divida -= mensal
    if divida >= 0:
        print(f'depois = {divida:.0f}')
    else:
        print(f'depois = 0')
    print('-----')
    pagamento += 1