"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados (keyword arguments) são passados para funções usando o nome do parâmetro,
enquanto argumentos não nomeados (positional arguments) são passados na ordem em que os parâmetros são definidos na função.
"""

def soma(x, y, z):
    #Define a função soma que recebe três argumentos: x, y e z
    print(f'{x=} y={y} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)  # Chamada da função com argumentos não nomeados
soma(y=2, z=3, x=1)  # Chamada da função com argumentos nomeados

print(1, 2, 3, sep='-')  # Chamada da função print com argumentos não nomeados