import datetime
ano = str(input('Qual ano quer analisar?')).strip()
resposta = int(ano)

hora = (datetime.datetime.now())
data = (hora.date())
yr = int(data.strftime("%Y"))

if resposta == 0:
    if yr % 4 == 0:
        print(f'{yr} é bissexto')
    else:
        print(f'{yr} não é bissexto')
else:
    if resposta % 4 == 0:
        print(f'{ano} é bissexto')
    else:
        print(f'{ano} não é bissexto')