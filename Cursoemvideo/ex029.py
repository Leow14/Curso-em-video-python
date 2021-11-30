from time import sleep
vel = str(input('Me diga sua velocidade:')).strip()
velocidade = int(vel)
multa = (velocidade - 81) * 8
sleep(1)
if velocidade >= 81:
    print(f'VOCÊ FOI MULTADO E DEVERÁ \nPAGAR {multa} REAIS DE MULTA')
else:
    pass

print('-=-' * 10)
print('Diriga com segurança!')