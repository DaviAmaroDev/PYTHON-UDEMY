import tkinter #tkinter é uma biblioteca para criar interfaces gráficas
from tkinter import font

#Botões da calculadora
valores_botoes = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

#Simbolos da calculadora de direita pra cima
simbolos_direita = ["÷", "×", "-", "+", "="]
simbolos_topo = ["AC", "+/-", "%",]

#Contagem de linhas e colunas
contagem_linhas = len(valores_botoes) #5
contagem_colunas = len(valores_botoes[0]) #4

#Cores dos botões da calculadora
cor_cinsa_claro = "#878787"
cor_preto = "#1A1A1A"
cor_cinsa_escuro = "#454545"
cor_laranja = "#009CCC"
cor_branco = "white"

#window setup
window = tkinter.Tk() #Cria a janela
window.title("Calculadora Complexa") #Titulo da janela
window.resizable(False, False) #Não permite redimensionar a janela

frame = tkinter.Frame(window) #Cria um frame dentro da janela
label = tkinter.Label(frame, text="0", font=font.Font(family="Arial", size=45), anchor="e", bg=cor_preto, fg=cor_branco, width=contagem_colunas) #Cria um label dentro do frame, 
#com o texto "0", fonte Arial tamanho 45, alinhado à direita, com fundo preto e texto branco

label.grid(row = 0, column = 0, columnspan = contagem_colunas, sticky="ew")

for row in range(contagem_linhas):
    for col in range(contagem_colunas):
        value = valores_botoes[row][col]
        button = tkinter.Button(frame, text=value, font=font.Font(family="Arial", size=30),
                                 width = contagem_colunas - 1, height = 1, 
                                  command=lambda value=value: button_clicked(value))
        if value in simbolos_topo:
            button.config(bg=cor_cinsa_claro, fg=cor_preto)
        elif value in simbolos_direita:
            button.config(bg=cor_laranja, fg=cor_branco)
        else:
            button.config(bg=cor_cinsa_escuro, fg=cor_branco)
        button.grid(row=row + 1, column=col)

frame.pack()

#A+B, A-B, A*B, A/B
A = "0"
operador = None
B = None

def clear_all():
    global A, B, operador
    A = "0"
    operador = None
    B = None
    
def button_clicked(value):
    global simbolos_direita, simbolos_topo, A, B, operador

    if value in simbolos_direita:
        if value == "=":
            if operador is not None and B is not None:
                if operador == "+":
                    A = str(float(A) + float(B))
                elif operador == "-":
                    A = str(float(A) - float(B))
                elif operador == "×":
                    A = str(float(A) * float(B))
                elif operador == "÷":
                    A = str(float(A) / float(B))
                label["text"] = A
                B = None
                operador = None
        else:
            if operador is None:
                operador = value
                A = label["text"]
                label["text"] = "0"
            else:
                if B is None:
                    B = label["text"]
                    if operador == "+":
                        A = str(float(A) + float(B))
                    elif operador == "-":
                        A = str(float(A) - float(B))
                    elif operador == "×":
                        A = str(float(A) * float(B))
                    elif operador == "÷":
                        A = str(float(A) / float(B))
                    label["text"] = A
                    B = None
                    operador = value
    elif value in simbolos_topo:
        if value == "AC":
            label["text"] = "0"
            A = "0"
            B = None
            operador = None
        elif value == "+/-":
            if label["text"] != "0":
                if label["text"][0] == "-":
                    label["text"] = label["text"][1:]
                else:
                    label["text"] = "-" + label["text"]
        elif value == "%":
            if operador is None:
                A = str(float(A) / 100)
                label["text"] = A
            else:
                B = str(float(label["text"]) / 100)
                label["text"] = B
    else: #digitos ou .
        if value == ".":
            if value not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0": #0
                label["text"] = value
            else:
                label["text"] += value #anexa o digito ao final do texto do label

#centro da janela
window.update() #atualiza a janela com novos tamanhos de dimensão
window_width = window.winfo_width() #pega a largura da janela
window_height = window.winfo_height() #pega a altura da janela
screen_width = window.winfo_screenwidth() #pega a largura da tela
screen_height = window.winfo_screenheight() #pega a altura da tela

window_x = (screen_width // 2) - (window_width // 2) #calcula a posição x da janela
window_y = (screen_height // 2) - (window_height // 2) #calcula a posição y da janela

#formato "(w) * (h) * (x) * (y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}") #define a geometria da janela

window.mainloop()