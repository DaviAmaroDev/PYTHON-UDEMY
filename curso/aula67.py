"""
Valores padrão para parâmetros de funções
Ao definir uma função, 
você pode atribuir valores padrão aos parâmetros. 
Isso significa que, se um argumento não for fornecido durante a chamada da função, 
o valor padrão será usado.
Refatorar: 
"""

def soma(x, y=None, z=None):
    if z is not None:
        print(f'{x=} y={y} {z=}', x + y + z)
    else:
        print(f'{x=} y={y}', x + y)

soma(1, 2)
soma(3, 5)
soma(100, 200)
soma(7, 9, 0)