from tkinter import *
from tkinter import messagebox

from classBancoDados import bd

class interfaceCliente:

    def __init__(self):
    
        #Font style and size
        fontStyle = 'Arial 12'

        self.window = Tk()
        self.window.title('LD- Cadastrar Cliente')
        self.window.geometry('300x250')
        self.window.resizable(False, False)

        #Labels
        self.lblNome = Label(self.window, text='Nome:', font=fontStyle)
        self.lblNome.place(x=30, y=30)

        self.lblIdade = Label(self.window, text='CPF:', font=fontStyle)
        self.lblIdade.place(x=30, y=90)

        self.lblCpf = Label(self.window, text='DATA DE NASCIMENTO:', font=fontStyle)
        self.lblCpf.place(x=30, y=150)

        #entry
        self.etNome = Entry(self.window, font=fontStyle)
        self.etNome.place(x=30, y=50)

        self.etCpf = Entry(self.window, font=fontStyle)
        self.etCpf.place(x=30, y=110)

        self.etNasc = Entry(self.window, font=fontStyle)
        self.etNasc.place(x=30, y=170)

        #Menu
        myMenu = Menu(self.window, tearoff=0)

        fileMenu = Menu(myMenu)

        fileMenu.add_command(label='Salvar', command=self.saveAllData)
        fileMenu.add_command(label='Descartar', command=self.clearCamps)
        fileMenu.add_command(label='Sair', command=exit)

        myMenu.add_cascade(label='File', menu=fileMenu)
        
        self.window.config(menu=myMenu)
        self.window.mainloop()

    #gets
    def getEntryNome(self):
        return self.etNome.get()

    def getEntryCpf(self):
        return self.etCpf.get()

    def getEntryNasc(self):
        return self.etNasc.get()

    #salvar cliente
    def saveAllData(self):
        dataBase = bd()
        dataBase.insertDataUser(1, self.getEntryNome(), self.getEntryCpf(), self.getEntryNasc())

        messagebox.showinfo('','CADASTRADO COM SUCESSO')
        self.clearCamps()

    #limpar campos
    def clearCamps(self):
        self.etNome.delete(0, END)
        self.etCpf.delete(0, END)
        self.etNasc.delete(0, END)

        self.etNome.focus()

interfaceCliente()