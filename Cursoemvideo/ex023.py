numero = int(input('Digite um número:'))
print(f'Analisando o número {numero}')
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print(f'O número tem {u} unidades')
print(f'O número tem {d} dezenas')
print(f'O número tem {c} centenas')
print(f'O número tem {m} milhares')