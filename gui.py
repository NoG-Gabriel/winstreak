from tkinter import ttk
from tkinter import *

contador = 0

def incrementar():
    global contador

    contador += 1
    contador_var.set(contador)

def zerar():
    global contador

    contador = 0
    contador_var.set(contador)

raiz = Tk()
raiz.title("Contador do Diabo")
janela = ttk.Frame(raiz, padding=5)
janela.grid()

contador_var = IntVar(value=contador)
ttk.Label(janela, text="Win-Streak =").grid(column=1, row=0,  padx=(0, 5), pady=(0, 15))
ttk.Label(janela, textvariable=contador_var).grid(column=1, row=0, columnspan=2, pady=(0, 15))

ttk.Button(janela, text="Ganhei!", command=incrementar).grid(column=0, row=1, padx=5)
ttk.Button(janela, text="Zerei Veyr", command=zerar).grid(column=1, row=1, padx=5)
ttk.Button(janela, text="Quit", command=raiz.destroy).grid(column=2, row=1, padx=5)

raiz.mainloop()