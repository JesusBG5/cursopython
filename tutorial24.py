from tkinter import *

def calcular():
	n1 = num1.get()
	n2 = num2.get()
	op = opcion.get()
	if op==1:
		res.set(n1+n2)
	elif op==2:
		res.set(n1-n2)
	elif op==3:
		res.set(n1*n2)
	elif op==4:
		res.set(n1/n2)


ventana = Tk()
num1 = DoubleVar()
num2 = DoubleVar()
res = DoubleVar()
opcion = IntVar()
ventana.geometry("300x300")
ventana.title("Radiobutton")

#Etiquetas
etiqueta1 = Label(ventana,text="Valor 1: ")
etiqueta1.place(x=10,y=40)
etiqueta2 = Label(ventana,text="Valor 2: ")
etiqueta2.place(x=10,y=70)
etiquetaR = Label(ventana,text="Resultado: ",textvariable=res)
etiquetaR.place(x=10,y=200)
#Cajas
caja1 = Entry(ventana,textvariable=num1)
caja1.place(x=100,y=40)
caja2 = Entry(ventana,textvariable=num2)
caja2.place(x=100,y=70)
#Boton
boton1 = Button(ventana,text="Calcular",command=calcular)
boton1.place(x=30,y=160)
#RadioButton
radio1 = Radiobutton(ventana,text="Suma",value=1,variable=opcion)
radio1.place(x=10,y=100)
radio2 = Radiobutton(ventana,text="Resta",value=2,variable=opcion)
radio2.place(x=110,y=100)
radio3 = Radiobutton(ventana,text="Multiplicación",value=3,variable=opcion)
radio3.place(x=10,y=130)
radio4 = Radiobutton(ventana,text="División",value=4,variable=opcion)
radio4.place(x=110,y=130)
ventana.mainloop()