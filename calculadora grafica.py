import tkinter as tk

# Função para adicionar número ou operador ao visor
def adicionar_texto(valor):
    entrada_texto.set(entrada_texto.get() + str(valor))

# Função para calcular o resultado
def calcular():
    try:
        resultado = str(eval(entrada_texto.get()))
        entrada_texto.set(resultado)
    except Exception as e:
        entrada_texto.set("Erro")

# Função para limpar o visor
def limpar():
    entrada_texto.set("")

# Criação da janela principal
janela = tk.Tk()
janela.title("Calculadora")

# Variável de controle para o visor
entrada_texto = tk.StringVar()

# Visor da calculadora
visor = tk.Entry(janela, textvariable=entrada_texto, font=("Arial", 24), bd=10, insertwidth=4, width=14, borderwidth=4, justify='right', state='readonly', disabledbackground='white')
visor.grid(row=0, column=0, columnspan=4)

# Botões para números e operadores
botoes = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', 'C', '=', '+'
]

row_val = 1
col_val = 0

# Adicionar botões à interface
for botao in botoes:
    if botao == '=':
        tk.Button(janela, text=botao, padx=20, pady=20, font=("Arial", 16), command=calcular).grid(row=row_val, column=col_val)
    elif botao == 'C':
        tk.Button(janela, text=botao, padx=20, pady=20, font=("Arial", 16), command=limpar).grid(row=row_val, column=col_val)
    else:
        tk.Button(janela, text=botao, padx=20, pady=20, font=("Arial", 16), command=lambda b=botao: adicionar_texto(b)).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Iniciar o loop principal da interface gráfica
janela.mainloop()
