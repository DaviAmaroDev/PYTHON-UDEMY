#Formatação de strings com f-strings
nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print(f"Olá, {nome} {sobrenome}!")
print(f"Olá, {nome} {sobrenome: >10}!")
print(f"Olá, {nome} {sobrenome: <10}!")
print(f"Olá, {nome} {sobrenome: ^10}!")