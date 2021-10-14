from tkinter import *
from tkinter import messagebox
import tutorial37 as t

class Interfaz:

	def __init__(self,ventana):
		self.ventana = ventana
		self.ventana.title("Agenda")
		self.ventana.geometry("400x400")
		self.nombre = StringVar()
		self.edad = IntVar()
		Label(ventana,text="Nombre: ").place(x=5,y=10)
		Entry(ventana,textvariable=self.nombre).place(x=70,y=10)
		Label(ventana,text="Edad: ").place(x=5,y=80)
		Entry(ventana,textvariable=self.edad).place(x=70,y=80)
		Button(ventana,command=self.guardar,text="Guardar").place(x=70,y=150)

	def guardar(self):
		con = t.Conexion()
		con.insertar(self.nombre.get(),self.edad.get())
		messagebox.showinfo("Alta","Datos registrados :D ")

obj = Interfaz(Tk())
obj.ventana.mainloop()