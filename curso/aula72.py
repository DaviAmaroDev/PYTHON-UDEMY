def multiplicar(*args):
    total = 0
    for numero in args:
        total *= numero
    return total
multiplicacao = multiplicar(10, 2, 3, 4, 5)
print(multiplicacao)

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'O número {numero} é par'
    else:
        return f'O número {numero} é ímpar'


print(par_impar(10))
print(par_impar(1))
print(par_impar(2))
print(par_impar(5))
print(par_impar(3))
