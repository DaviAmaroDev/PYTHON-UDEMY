"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - indices e fatiamento
Métodos úteis:
    append - Adiciona um elemento ao final da lista
    insert - Adiciona um elemento em uma posição específica
    pop - Remove o último elemento da lista ou o elemento de uma posição específica
    del - Remove um elemento de uma posição específica
    clear - limpa a lista
    extend - Adiciona vários elementos ao final da lista
    + - concatena listas
Create Read Update Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_d = lista_a.extend(lista_b)
print(lista_c)
print(lista_d)