import tkinter as tk

def press(num):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(num))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Erro")

# Configurar a janela principal
root = tk.Tk()
root.title("Calculadora")

# Widget de entrada
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

# Botões
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, command=lambda b=button: press(b) if b != '=' else calculate()).grid(row=row_val, column=col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Botão de Limpar
tk.Button(root, text='C', padx=20, pady=20, command=clear).grid(row=5, column=0, columnspan=4)

root.mainloop()