import tkinter #tkinter é uma biblioteca para criar interfaces gráficas
from tkinter import font

#Botões da calculadora
button_values = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

#Simbolos da calculadora de direita pra cima
right_symbols = ["÷", "×", "-", "+", "="]
top_symbols = ["AC", "+/-", "%",]

#Contagem de linhas e colunas
row_count = len(button_values) #5
col_count = len(button_values[0]) #4

#Cores dos botões da calculadora
color_light_grey = "#878787"
color_black = "#1A1A1A"
color_dark_grey = "#454545"
color_orange = "#009CCC"
color_white = "white"

#window setup
window = tkinter.Tk() #Cria a janela
window.title("Complex Calc") #Titulo da janela
window.resizable(False, False) #Não permite redimensionar a janela

frame = tkinter.Frame(window) #Cria um frame dentro da janela
label = tkinter.Label(frame, text="0", font=font.Font(family="Arial", size=45), anchor="e", bg=color_black, fg=color_white, width=col_count) #Cria um label dentro do frame, 
#com o texto "0", fonte Arial tamanho 45, alinhado à direita, com fundo preto e texto branco

label.grid(row = 0, column = 0, columnspan = col_count, sticky="ew")

for row in range(row_count):
    for col in range(col_count):
        value = button_values[row][col]
        button = tkinter.Button(frame, text=value, font=font.Font(family="Arial", size=30),
                                 width = col_count - 1, height = 1, 
                                  command=lambda value=value: button_clicked(value))
        if value in top_symbols:
            button.config(bg=color_light_grey, fg=color_black)
        elif value in right_symbols:
            button.config(bg=color_orange, fg=color_white)
        else:
            button.config(bg=color_dark_grey, fg=color_white)
        button.grid(row=row + 1, column=col)

frame.pack()

#A+B, A-B, A*B, A/B
A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int(num)
    return str(num)

def button_clicked(value):
    global right_symbols, top_symbols, A, B, operator

    if value in right_symbols:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                if operator == "+":
                    label["text"] = remove_zero_decimal(numA + numB)
                elif operator == "-":
                    label["text"] = remove_zero_decimal(numA - numB)
                elif operator == "×":
                    label["text"] = remove_zero_decimal(numA * numB)
                elif operator == "÷":
                    label["text"] = remove_zero_decimal(numA / numB)

                clear_all()
        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = "0"

    elif value in top_symbols:
        if value == "AC":
            label["text"] = "0"
            A = "0"
            B = None
            operator = None
        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)
        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)
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