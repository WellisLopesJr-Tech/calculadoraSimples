#Importar da Biblioteca
from tkinter import *
from tkinter import ttk

#Cores
cor1 = "#1f1e1e" #preto claro

janela = Tk()
janela.title("Calculadora")
janela.geometry("320x500") #Definir tamanhos e posições da janela
janela.config(bg=cor1)

#Dividir tela 
frame_tela = Frame(janela, width=320, height=70)
frame_tela.grid(row=0, column=0)


#Inicar o loop principal da interface gráfica no TKinder
janela.mainloop()




