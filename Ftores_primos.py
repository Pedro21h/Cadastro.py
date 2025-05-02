
def fatores_primos(num):
    fatores = []
    divisores = 2
    while divisores <= num:
        if num % divisores == 0:
            fatores.append(divisores)
            num = num // divisores
        else:
            divisores = divisores+1
    return fatores

#chamda da função:
num = int(input('digite um numero: '))
print (f'os fatores de {num} é {fatores_primos(num)}')
