#Exercicio 1
"""
entrada = input('Digite um número: ')

if entrada.isdigit():
    numero = int(entrada)
    if numero % 2 == 0:
        print(f'O número {numero} é par.')
    else:
        print(f'O número {numero} é ímpar.')
else:
    print('Entrada inválida. Por favor, digite um número inteiro.')
"""

#Exercicio 2
"""
entrada = input('Digite a hora em numeros inteiros: ')

try:
    hora = int(entrada)
    if 0 <= hora < 12:
        print('Bom dia!')
    elif 12 <= hora < 18:
        print('Boa tarde!')
    elif 18 <= hora < 24:
        print('Boa noite!')
    else:
        print('Hora inválida. Por favor, digite um número entre 0 e 23.')
except ValueError:
    print('Entrada inválida. Por favor, digite um número inteiro.')
"""

#Exercicio 3
"""
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto.')
    elif tamanho_nome == 5 or tamanho_nome == 6:
        print('Seu nome é normal.')
    else:
        print('Seu nome é muito grande.')    
else:
    print('Digite mais uma letra para o nome.')
"""