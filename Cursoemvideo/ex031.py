vb = str(input('Quantos KM tem sua viagem?')).strip()
va = float(vb)
pc = va*0.50
pl = va*0.45
if va >= 200:
    print(f'A viagem custarĂ¡ {pl}')
else:
    print(f'A viagem custarĂ¡ {pc}')