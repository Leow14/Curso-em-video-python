aa = input('\033[7:34:40mPrimeiro segmento:').strip()
bb = input('Segundo segmento:').strip()
cc = input('\033[7:34:40mTerceiro segmento:\033[m').strip()
a = float(aa)
b = float(bb)
c = float(cc)

if a + b > c:
    if a + c > b:
        if b + c > a:
            print('Você PODE formar um triângulo')
        else:
            print('Você NÃO PODE formar um triângulo')
    else:
        print('Você NÃO PODE formar um triângulo')
else:
    print('Você NÃO PODE formar um triângulo')