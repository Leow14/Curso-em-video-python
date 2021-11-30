import math

ang = int(input('Digite o ângulo:'))
ran = math.radians(ang)
sen = math.sin(ran)
co = math.cos(ran)
ta = math.tan(ran)

print('No ângulo de {} graus, o seno equivale a {:.3} \nO cosseno equivale a {:.3} \nA tangente equivale a {:.3}' .format(ang, sen, co, ta))
