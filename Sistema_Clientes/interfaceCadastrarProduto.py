from tkinter import *
from tkinter import messagebox

from classBancoDados import bd

class interfaceProduto:

    def __init__(self):
    
        #Font style and size
        fontStyle = 'Arial 12'

        self.window = Tk()
        self.window.title('LD- Cadastrar Cliente')
        self.window.geometry('300x280')
        self.window.resizable(False, False)

        #Labels
        self.lblCod = Label(self.window, text='CÓDIGO DE BARRAS:', font=fontStyle)
        self.lblCod.place(x=30, y=30)

        self.lblNome = Label(self.window, text='NOME:', font=fontStyle)
        self.lblNome.place(x=30, y=90)

        self.lblValor = Label(self.window, text='VALOR:', font=fontStyle)
        self.lblValor.place(x=30, y=150)

        self.lblStock = Label(self.window, text='ESTOQUE:', font=fontStyle)
        self.lblStock.place(x=30, y=210)

        #entry
        self.etCod = Entry(self.window, font=fontStyle)
        self.etCod.place(x=30, y=50)

        self.etNome = Entry(self.window, font=fontStyle)
        self.etNome.place(x=30, y=110)

        self.etValor = Entry(self.window, font=fontStyle)
        self.etValor.place(x=30, y=170)

        self.etStock = Entry(self.window, font=fontStyle)
        self.etStock.place(x=30, y=230)

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
    def getEntryCod(self):
        return self.etCod.get()

    def getEntryNome(self):
        return self.etNome.get()

    def getEntryValor(self):
        return self.etValor.get()

    def getEntryStock(self):
        return self.etStock.get()

    #salvar cliente
    def saveAllData(self):
        dataBase = bd()
        dataBase.insertDataProduct(self.getEntryCod(), self.getEntryNome().upper(), self.getEntryValor(), self.getEntryStock())
        #dataBase.insertDataProduct('001', 'TECLADO', '50', '5')
        
        messagebox.showinfo('','CADASTRADO COM SUCESSO')
        self.clearCamps()

    #limpar campos
    def clearCamps(self):
        self.etNome.delete(0, END)
        self.etCod.delete(0, END)
        self.etValor.delete(0, END)
        self.etStock.delete(0, END)

        self.etNome.focus()

interfaceProduto()