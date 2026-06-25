contador = 0

while contador <= 100:
    contador += 1

    if contador == 6:
        print('Encontramos o número 6, saindo do loop')
        continue

    if contador >= 10 and contador <= 27:
        print(f'Número {contador} ignorado, pulando para o próximo')
        continue

    print(contador)

    if contador == 40:
        print('Encontramos o número 40, saindo do loop')
        break