from tkinter import *

class interfaceSales:

    def __init__(self):

        self.window = Tk()
        self.window.geometry('900x600+260+100')
        self.window.title('Sales')

        self.lblSalesSector = Label(text='SALES SECTOR', width=500, height=1, font='Arial 25 bold', fg='white', bg='DarkRed')
        self.lblSalesSector.pack()

        self.banner = Label(text='', width=500, height=1, font='Arial 25 bold', fg='white', bg='DarkRed')
        self.banner.place(x=0, y=550)

        self.lblBarCod = Label(text='Bar Code:', font='Arial 15 bold')
        self.lblBarCod.place(x=10, y=70)

        self.lblTotal = Label(text='TOTAL: ', fg='black', bg='DarkRed', font='Arial 18 bold')
        self.lblTotal.place(x=680, y=553)

        self.lblAmount = Label(text='AMOUNT: ', fg='black', bg='DarkRed', font='Arial 18 bold')
        self.lblAmount.place(x=420, y=553)

        self.lblProducts = Label(text='PRODUCTS ALL', font='Arial 18 bold', bg='DarkRed', fg='white', height=1, width=35)
        self.lblProducts.place(x=410, y=104)

        self.lblProductsInformation = Label(text='Product Information', font='Arial 12 bold')
        self.lblProductsInformation.place(x=10, y=155)

        self.paintingInformation = Label(text='', font='Arial 18 bold', bg='DarkRed', fg='white', width=28, height=13)
        self.paintingInformation.place(x=10, y=179)

        #all products
        self.scrollbar = Scrollbar(self.window)
        self.scrollbar.pack(side="right", fill="y")

        self.listbox = Listbox(self.window, height=24, width=57, yscrollcommand=self.scrollbar.set, font='Courier 10', bg='LemonChiffon')
        self.listbox.place(x=410, y=150)

        #variable
        self.lblTotalVariable = Label(text='00,00', fg='white', bg='DarkRed', font='Arial 18 bold')
        self.lblTotalVariable.place(x=780, y=553)

        self.lblAmountVariable = Label(text='0', fg='white', bg='DarkRed', font='Arial 18 bold')
        self.lblAmountVariable.place(x=550, y=553)

        self.etCodProd = Entry(font='Arial 25 bold', fg='white', bg='DarkRed')
        self.etCodProd.place(x=10, y=100)

        #focar no cogio de barras
        self.etCodProd.focus()

        #sequencia de dados 
        self.listbox.insert("end", 'CODE           PROD.         VAL UNT.  QUANT  VAL TOTAL')

        self.scrollbar.config(command=self.listbox.get)
        self.window.mainloop()

interfaceSales()