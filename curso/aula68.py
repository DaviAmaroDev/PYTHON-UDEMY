"""
Escopo de funções em Python
Escopo significa o local onde aquele codigo vai atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o codigo é alcançavel, ou seja, o escopo global é o escopo do programa.
O escopo local é o escopo onde apenas o codigo dentro da função é alcançavel.
"""

x = 1

def escopo():
    global x
    x = 10
    
    def outra_funcao():
        x = 11
        y = 2
        print(x, y)
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)