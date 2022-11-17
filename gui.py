import tkinter as tk
import tkinter.font as tkFont
from logic import upload

# Definindo a janela principal
win = tk.Tk()
win.title("AutomatizAIChE")
win.geometry('500x500')
win.configure(bg = '#c1b56f')

# Fonte da AIChE UFRJ
fontaiche = tkFont.Font(family="Lato", weight='bold')

# Texto principal
tst = tk.Label(win, text= "Anexe o banco de dados das pessoas aprovadas", background='#c1b56f', foreground='#0d275a')
tst.place(x = 60, y = 100)
tst.configure(font=fontaiche)

# Botão principal
btn = tk.Button(win, text = "Selecione o arquivo",command=upload, background='#0d275a', foreground='#c1b56f')
btn.configure(font=fontaiche)
btn.place(x = 170, y = 200)
win.mainloop()
