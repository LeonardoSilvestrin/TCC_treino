from tkinter import *
from PIL import ImageTk

#widgets = GUI elements: botão, caixa de texto, etc
#janela = container de widget


janela = Tk() #instanciar uma janela
janela.geometry("400x400")
janela.title("A janela dos patos")
icone = ImageTk.PhotoImage(file='C:\\Users\\Leonardo\\Desktop\\Engenharia\\TCC\\Python\\git\\Treino_leo\\Treino_básico\\pato.jpg')
janela.iconphoto(True,icone)
label = Label(janela,text = "Olá Mundo",font = ('Times New Roman',40,'bold'),fg = '#000FF0', bg = "grey")
label.place(x=90,y=150)
janela.mainloop() #coloca a janela na tela

