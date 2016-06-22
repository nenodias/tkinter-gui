import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename

from compactador import *
from threading import Thread


class Aplicacao(Frame):

    def __init__(self,*args, **kwargs):
        super(Aplicacao, self).__init__(*args, **kwargs)
        self.pack()

        self.botao_adicionar = Button(self, text='Adicionar', command=self.adicionar, bd=3)
        self.botao_adicionar['font'] = ('Arial', 12) # adiciona uma fonte
        self.botao_adicionar.pack(pady=10, padx=30, side='left')

    def adicionar(self):
        print('Do anithing')


root = Tk() # obtém uma instância de Tk
root.title('Compactador de arquivos') # coloca um titulo na janela

#Colocar Ícone
icone = tkinter.Image("photo", file="icone.png")
root.tk.call('wm','iconphoto',root._w,icone)

root.geometry('400x300') # ajusta o tamanho
root.resizable(width=FALSE, height=FALSE) # desabilita o redimensionamento da janela
app = Aplicacao(root) # passa instancia de Tk para classe Aplicacao
root.mainloop()