from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def cambiar():
	comida = combo.get()
	if comida=="Frutas":
		combo2["values"]=("Manzana","Mandarina","Naranja")
	if comida=="Verduras":
		combo2["values"]=("Lechuga","Cebolla")
	if comida=="Carnes":
		combo2["values"]=("Pollo","Pescado","Res")
	combo2.current(0)

ventana = Tk()
ventana.geometry("300x300")
ventana.title("Combobox")

etiqueta = Label(ventana,text="¿Qué deseas comer?")
etiqueta.place(x=100,y=40)

combo = ttk.Combobox(ventana,state="readonly")
combo.place(x=100,y=70)
combo["values"]=("Frutas","Verduras","Carnes")
combo.current(0)

boton = Button(ventana,text="Cargar",command=cambiar)
boton.place(x=100,y=100)

combo2 = ttk.Combobox(ventana,state="readonly")
combo2.place(x=100,y=130)

ventana.mainloop()