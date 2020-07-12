#Tkinter Entradas/Etiquetas
from Tkinter import *

def calcular():
	cuadrado = num.get()*num.get()
	res.set("El cuadrado de " + str(num.get()) + " es: " + str(cuadrado))

ventana = Tk()
#StringVar , IntVar, DoubleVar
num = IntVar()
res = StringVar()
ventana.geometry("400x300")
#Etiqueta
textoN = Label(ventana,text="Escribe un numero: ")
textoN.place(x=150,y=10)
#Caja de texto
caja = Entry(ventana,textvariable=num)
caja.place(x=150,y=40)
#Etiqueta Resultado
textoR = Label(ventana,textvariable=res)
textoR.place(x=150,y=140)
#Boton
boton = Button(ventana,text="Calcular",command=calcular,bg="#006",fg="white")
boton.place(x=180,y=100)
ventana.mainloop()