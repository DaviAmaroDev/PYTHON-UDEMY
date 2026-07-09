"""
split e join com list e str
split - divide uma string em uma lista de substrings com base em um delimitador especificado.
join - combina uma lista de strings em uma única string, usando um delimitador especificado.
"""
frase = '   Olha só que      , coisa interessante!           '
lista_frases_cruas = frase.split(',')

lista_frases = []
for i, frase in enumerate(lista_frases_cruas):
    lista_frases.append(lista_frases_cruas[i].strip())

#print(lista_frases_cruas)
#print(lista_frases)
frases_unidas = ', '.join(lista_frases)
print(frases_unidas)