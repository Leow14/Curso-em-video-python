nome = input('Qual é o seu nome?').strip()
print(f'Seu nome em maiscula é {nome.upper()}')
print(f'Seu nome em minuscula é {nome.lower()}')
espaço = (len(nome) - nome.count(' '))

print(f'Seu nome tem {espaço} letras')
nomed = nome.split()
print(f'E seu primeiro nome é {nomed[0]} e tem {len(nomed)} letras')