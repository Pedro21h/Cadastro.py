import random
n = (random.randint(1,100))
num = int(input('escreva um numero de 1 a 100: '))

if num == n:
    print('parabens vc acertou')
else:
    print('vc errou')
    print(f'o numero certo era {n}')
