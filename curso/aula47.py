"""
Faça um jogo para o usuario adivinhar qual palavra é certa
-Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuario digitar apenas uma letra por vez.
-Se o usuario acertar a letra, você vai mostrar a letra na tela, caso contrario, você vai mostrar um traço no lugar da letra.
-Faça a contagem de tentativas e mostre para o usuario quantas tentativas ele ainda tem.
"""
import os

palavra_secreta = 'elefante'
letras_acertadas = ''
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ')
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra in palavra_secreta:
        if letra in letras_acertadas:
            palavra_formada += letra
        else:
            palavra_formada += '_'

    print(f'Palavra formada: {palavra_formada}')

    if palavra_formada == palavra_secreta:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Parabéns! Você acertou a palavra secreta.')
        print('A palavra secreta era:', palavra_secreta)
        print('Número de tentativas:', numero_tentativas)
        letras_acertadas = ''
        numero_tentativas = 0
        break