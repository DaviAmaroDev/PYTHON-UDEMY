"""
Listas de listas e seus indices
"""
salas = [
    #0          1
    ['Maria', 'Helena'], #0
    #0
    ['Elaine',], #1
    #0          1          2
    ['Luiz', 'João', 'Eduarda', ], #2
]
#print(salas[1][0]) # Elaine
#print(salas[2][2]) # Eduarda

for sala in salas:
    for aluno in sala:
        print(aluno, end=' ')
    print()