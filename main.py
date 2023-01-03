from tkinter import *
from tkinter import ttk

# cores

co0 = '#ffffff' #branco
co1 = '#4065a1' #laranja
co2 = '#FFB74D' #azul
co3 = '#000000' #preto

janela = Tk()
janela.title('')
janela.geometry('295x230')
janela.configure(bg='orange') #abre a janela e confg 


#Dividir a janela em duas partes

frame_cima= Frame(janela, width=295, height=50, bg=co2, pady=0, padx=0, relief='flat')
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo= Frame(janela, width=295, height=180, bg=co2, pady=0, padx=0, relief='flat')
frame_baixo.grid(row=1, column=0, sticky=NSEW)

#Confif frame_cima

app_nome = Label(frame_cima, text='Calculadora de IMC', width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold '), bg=co2, fg=co0)
app_nome.place(x=0, y=0)

app_nome = Label(frame_cima, text='', width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1 '), bg=co0, fg=co2)
app_nome.place(x=0, y=35)

#Função calcular

def calcular():
    peso = float(e_peso.get()) #.get() deixa atribuir o valor(os parametros sao passados no cabeçalho da requisição)
    altura = float(e_altura.get())

    imc = peso / altura**2 #peso dividido pela altura ao quadrado, variavel com valor de uma conta 
    resultado = imc #variavel de valor 
    
    #condição if elif else.

    if resultado > 18.5:
        l_resultado_texto['text'] = "Seu IMC é: Abaixo do peso"
        
    elif resultado >= 18.5 and resultado < 25:
        l_resultado_texto['text'] = "Seu IMC é: Normal"
        
    elif resultado >= 25 and resultado > 30:
        l_resultado_texto['text'] = "Seu IMC é: Sobrepeso"
        
    else:
        l_resultado_texto['text'] = 'Seu IMC é: Obesidade'


    l_resultado['text'] = "{:.{}f}".format(resultado, 2)

 

#config frame_baixo

l_peso = Label(frame_baixo, text='Insira seu peso', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold '), bg=co2, fg=co0)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)
e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold '), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text='Insira sua altura', height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold '), bg=co2, fg=co0)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)
e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold '), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_baixo, text='---', width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold '), bg=co1, fg=co0)
l_resultado.place(x=175, y=10)

l_resultado_texto = Label(frame_baixo, text='', width=37, height=1, padx=0, pady=12, relief='flat', anchor='center', font=('Ivy 10 bold '), bg=co1, fg=co0)
l_resultado_texto.place(x=0, y=90)

b_calcular = Button(frame_baixo, command=calcular,  text='Calcular', width=34, height=1, overrelief=SOLID, relief='raised', anchor='center', font=('Ivy 10 bold '), bg=co1, fg=co0)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)


janela.mainloop()

# Oque cada linha faz:
# import Tkinter dev para interfaces graficas.
