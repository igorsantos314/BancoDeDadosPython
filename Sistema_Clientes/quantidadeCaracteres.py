from tkinter import *

def on_write(*args):
    s = var.get()
    if len(s) > 11:
        print('Codigo de Barras')

root = Tk()

var = StringVar()
var.trace("w", on_write) # rastrear valor da variavel e executar funcao de validacao quando mudar

entrada = Entry(root, textvariable=var)
entrada.pack()
root.mainloop()