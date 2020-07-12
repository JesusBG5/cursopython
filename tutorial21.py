#Botones Tkinter
from Tkinter import *

def cambio():
	#   r g b  0-f   0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f
	ventana.config(bg="#006")
	boton1.config(bg="#22d")
	boton1.config(fg="#fff")
	ventana.iconify()

def calcular():
	print("El cuadrado de 5 es: " + str(5*5))

ventana = Tk()
ventana.geometry("400x300")
boton1 = Button(ventana,text="Calcular",command=calcular)
boton1.place(x=20,y=20)
ventana.mainloop()