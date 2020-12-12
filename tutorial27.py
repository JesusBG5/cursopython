from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def cambiar():
	mes = int(combo.get())
	if mes==1:
		messagebox.showinfo("Mes","Enero")
	if mes==2:
		messagebox.showinfo("Mes","Febrero")
	if mes==3:
		messagebox.showinfo("Mes","Marzo")

ventana = Tk()
ventana.geometry("300x300")
ventana.title("Combobox")

etiqueta = Label(ventana,text="Transformación de número")
etiqueta.place(x=100,y=40)

combo = ttk.Combobox(ventana,state="readonly")
combo.place(x=100,y=70)
combo["values"]=("1","2","3","4","5","6","7","8","9","10","11","12")
combo.current(0)

boton = Button(ventana,text="Cambiar mes",command=cambiar)
boton.place(x=100,y=100)

ventana.mainloop()