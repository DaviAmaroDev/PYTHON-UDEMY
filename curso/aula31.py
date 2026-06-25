"""
Flags são variáveis booleanas (True ou False) que indicam se uma condição é verdadeira ou falsa. Elas são usadas para controlar o fluxo do programa, permitindo que certas partes do código sejam executadas apenas quando determinadas condições são atendidas.
exemplo:
is_raining = True
if is_raining: 
    print("Leve um guarda-chuva!")
else:
    print("Aproveite o dia ensolarado!")
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print("Faça algo")
else:
    print("Não faça nada")

if passou_no_if is None:
    print("Não passou no if")
else:
    print("Passou no if")