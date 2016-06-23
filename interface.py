import tkinter
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfilename, askopenfilenames

from compactador import *
from threading import Thread


class Aplicacao(Frame):

    def __init__(self,*args, **kwargs):
        super(Aplicacao, self).__init__(*args, **kwargs)
        self.pack()

        #Botão Adicionar
        self.botao_adicionar = Button(self, )
        self.botao_adicionar['text'] ='Adicionar'
        self.botao_adicionar['command'] = self.adicionar
        self.botao_adicionar['bd'] = 3 # borda
        self.botao_adicionar['font'] = ('Arial', 12)
        self.botao_adicionar.pack(pady=10, padx=30, side='left')

        #Botão Deletar
        self.botao_deletar = Button(self, text='Deletar')
        self.botao_deletar['command'] = self.deletar
        self.botao_deletar['bd'] = 3
        self.botao_deletar['font'] = ('Arial', 12)
        self.botao_deletar.pack(pady=10, padx=30, side='right')

        #Frame do ListBox
        self.frame2 = Frame()
        self.frame2['bd'] = 20
        self.frame2.pack()

        #Scrollbar
        self.scroll_bar_y = Scrollbar(self.frame2)
        self.scroll_bar_y.pack(side=RIGHT, fill=Y)

        self.scroll_bar_x = Scrollbar(self.frame2, orient=HORIZONTAL)
        self.scroll_bar_x.pack(side=BOTTOM, fill=X)

        #ListBox
        self.listbox = Listbox(self.frame2, width=50, height=10, selectmode=EXTENDED)
        self.listbox.pack()
        
        #Linkar scrollbars com listbox e os movimentos de coordenada x e y
        self.listbox.config(yscrollcommand=self.scroll_bar_y.set)
        self.scroll_bar_y.config(command=self.listbox.yview)
        self.listbox.config(xscrollcommand=self.scroll_bar_x.set)
        self.scroll_bar_x.config(command=self.listbox.xview)

        #Frame do Compactar
        self.frame3 = Frame()
        self.frame3.pack()

        #Botão Compactar
        self.botao_compactar = Button(self.frame3,text='Compactar')
        self.botao_compactar['command'] = self.compactar
        self.botao_compactar['bd'] = 3
        self.botao_compactar['font'] = ('Arial', 12)
        self.botao_compactar.pack()


    def adicionar(self):
        arquivos = list( askopenfilenames(title='Escolher arquivos') )
        if arquivos:
            for nome_arquivo in arquivos:
                self.listbox.insert(END, nome_arquivo)

    def deletar(self):
        items = self.listbox.curselection()
        if not items:
            messagebox.showinfo('Compactador', 'Selecione pelo menos 1 item')
        else:
            pos = 0
            for item in items:
                posicao_item = int(item) - pos
                self.listbox.delete(posicao_item, posicao_item)
                pos += 1

    def compactar(self):
        pass

root = Tk()
root.title('Compactador de arquivos')

#Colocar Ícone
icone = tkinter.Image("photo", file="icone.png")
root.tk.call('wm','iconphoto',root._w,icone)

root.geometry('400x320')
root.resizable(width=FALSE, height=FALSE) # desabilita o redimensionamento da janela
app = Aplicacao(root) # passa instancia de Tk para classe Aplicacao
root.mainloop()