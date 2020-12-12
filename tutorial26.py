#Spinbox
from tkinter import *
from tkinter import messagebox

def cambiar():
	#showinfo,showwarning,showerror,askquestion,askyesno,askokcancel,askyesnocancel,askretrycancel
	respuesta=messagebox.askyesno("Prueba 1","¿Estás seguro de querer cambiar el color?")
	if respuesta==True:
		ventana.configure(background=color.get())

ventana = Tk()
ventana.geometry("400x400")
ventana.title("Spinbox")
color = StringVar()

etiqueta1 = Label(ventana,text="Ejemplo 1")
etiqueta1.place(x=20,y=50)

lista = Spinbox(ventana,textvariable=color,values=("Blue","Yellow","Red","Green"))
lista.place(x=120,y=50)

etiqueta2 = Label(ventana,text="Ejemplo 2")
etiqueta2.place(x=20,y=150)

lista2 = Spinbox(ventana,from_=1900,to=2020)
lista2.place(x=120,y=150)

boton = Button(ventana,text="Cambiar",command=cambiar)
boton.place(x=50,y=200)

ventana.mainloop()