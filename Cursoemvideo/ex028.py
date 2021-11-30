import random
from time import sleep
pc = random.randint(1 , 5)
print('O computador irá escolher um número aleatório de 1 a 5 \nserá que você  consegue descobri-lo? ')
print('------------------------------------------------------')
sleep(1)
gues = input('Ele já escolheu! Qual é o seu palpite?').strip()
guess = int(gues)

if guess != pc:
    print(f'Você errou! O número escolhido pelo computador foi {pc}')
else:
    print(f'Parabéns!! Você acertou! O número escolhido pelo computador foi {pc}')
