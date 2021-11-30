pr = input('\033[7;38;42mDigite o primeiro valor:\033[m')
se = input('\033[7;38;42mDigite o segundo valor:\033[m')
te = input('\033[7;38;42mDigite o terceiro valor:\033[m')

if pr > se:
    if pr>te:
        print(f'\033[7;32;40m{pr} é o MAIOR valor\033[m')
        if te>se:
            print(f'\033[7;31;40m{se} é o MENOR valor\033[m')
        else:
            print(f'\033[7;31;40m{te} é o MENOR valor\033[m')
    else:
        print(f'\033[7;32;40m{te} é o MAIOR valor\033[m')
        if pr>se:
            print(f'\033[7;31;40m{se} é o MENOR valor\033[m')
        else:
            print(f'\033[7;31;40m{pr} é o MENOR valor\033[m')
else:
    if se>te:
        print(f'\033[7;32;40m{se} é o MAIOR valor\033[m')
        if te>pr:
            print(f'\033[7;32;41m{pr} é o MENOR valor\033[m')
        else:
            print(f'\033[7;32;41m{te} é o MENOR valor\033[m')
    else:
        print(f'\033[7;32;40m{te} é o MAIOR valor\033[m')
        if se>pr:
            print(f'\033[7;32;41m{pr} é o MENOR valor\033[m')
        else:
            print(f'\033[7;32;41m{se} é o MENOR valor\033[m')