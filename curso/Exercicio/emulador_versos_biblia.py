versos = [
    "João 3:16: Porque Deus tanto amou o mundo que deu o seu Filho Unigênito, para que todo o que nele crer não pereça, mas tenha a vida eterna.",
    "Salmos 23:1: O Senhor é o meu pastor; nada me faltará.",
    "1 Coríntios 13:4-7: O amor é paciente, o amor é bondoso...",
    "Jeremias 29:11: Porque sou eu que conheço os planos que tenho para vocês... planos de dar a vocês esperança e um futuro.",
    "Filipenses 4:13: Posso todas as coisas naquele que me fortalece."
]

def exibir_versos():
    global verso_escolhido
    verso_escolhido = input("Pressione Enter para exibir um verso da Bíblia..."
    "Digite '1' a '5' para escolher um verso específico: ")
    if verso_escolhido == "1":
        print(versos[0])
    elif verso_escolhido == "2":
        print(versos[1])
    elif verso_escolhido == "3":
        print(versos[2])
    elif verso_escolhido == "4":
        print(versos[3])
    elif verso_escolhido == "5":
        print(versos[4])
    else:
        print("Opção inválida. Por favor, escolha um número de 1 a 5.")

    verso_escolhido = input("Deseja exibir outro verso? (s/n): ")
    if verso_escolhido.lower() == "s":
        exibir_versos()
    else:
        print("Obrigado por usar o emulador de versos da Bíblia!")
        quit()

exibir_versos()