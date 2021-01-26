from tkinter import *
from tkinter import ttk

def prueba():
	print("Hola")

ventana = Tk()

panel = ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

tab1 = ttk.Frame(panel)
panel.add(tab1,text="Etiquetas")

tab2 = ttk.Frame(panel)
panel.add(tab2,text="Botones")
#Pestaña 1
etiqueta = Label(tab1,text="Recuerda que las etiquetas es con la clase Label")
etiqueta.place(x=20,y=20)
#Pestaña 2
etiqueta2 = Label(tab2,text="Para botones la clase es Button")
boton = Button(tab2,text="Prueba",command=prueba)
etiqueta2.place(x=20,y=20)
boton.place(x=20,y=50)

ventana.geometry("400x400")
ventana.title("Pestañas")
ventana.mainloop()