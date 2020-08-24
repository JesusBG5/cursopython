#Tkinter Calculadora
from tkinter import *

#Funciones de la calculadora

def suma():
	s = num1.get() + num2.get()
	res.set("La suma es: " + str(s))

def resta():
	r = num1.get() - num2.get()
	res.set("La resta es: " + str(r))

def multiplicacion():
	m = num1.get() * num2.get()
	res.set("La multiplicacion es: " + str(m))

def division():
	d = num1.get() / num2.get()
	d = round(d,3)
	res.set("La division es: " + str(d))


ventana = Tk()
# Variables para el formulario
res = StringVar()
res.set("Resultado : ")
num1 = DoubleVar()
num2 = DoubleVar()

ventana.geometry("500x400")
ventana.config(bg="steelblue")
#Etiquetas
textoNum1 = Label(ventana,text="Escribe un numero: ",bg="steelblue",fg="white")
textoNum1.place(x=30,y=10)

textoNum2 = Label(ventana,text="Escribe otro numero: ",bg="steelblue",fg="white")
textoNum2.place(x=30,y=70)

textoRes = Label(ventana,textvariable=res,bg="steelblue",fg="white")
textoRes.place(x=30,y=230)

#Cajas de texto

cajaNum1 = Entry(ventana,textvariable=num1)
cajaNum1.place(x=30,y=40)

cajaNum2 = Entry(ventana,textvariable=num2)
cajaNum2.place(x=30,y=100)

#Botones
botonSuma = Button(ventana,text="+",bg="#003",fg="white",command=suma)
botonSuma.place(x=30,y=150)

botonResta = Button(ventana,text="-",bg="#003",fg="white",command=resta)
botonResta.place(x=80,y=150)

botonMult = Button(ventana,text="*",bg="#003",fg="white",command=multiplicacion)
botonMult.place(x=130,y=150)

botonDiv = Button(ventana,text="/",bg="#003",fg="white",command=division)
botonDiv.place(x=180,y=150)

ventana.mainloop()