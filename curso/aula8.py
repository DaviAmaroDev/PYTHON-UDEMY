nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura em metros: '))
ano_nascimento = 2026 - idade
maior_idade = idade >= 18

print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Altura em metros:', altura)
print('Ano de nascimento:', ano_nascimento)
print('É maior de idade?', maior_idade)