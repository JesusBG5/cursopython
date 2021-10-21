from tkinter import *
from tkinter import messagebox
import tutorial37 as t
from tkinter import ttk

class Interfaz:

	def __init__(self,ventana):
		self.ventana = ventana
		self.ventana.title("Agenda")
		self.ventana.geometry("700x400")
		self.nombre = StringVar()
		self.edad = IntVar()
		Label(ventana,text="Nombre: ").place(x=5,y=10)
		Entry(ventana,textvariable=self.nombre).place(x=70,y=10)
		Label(ventana,text="Edad: ").place(x=5,y=80)
		Entry(ventana,textvariable=self.edad).place(x=70,y=80)
		Button(ventana,command=self.guardar,text="Guardar").place(x=70,y=150)
		self.consultar()

	def guardar(self):
		con = t.Conexion()
		con.insertar(self.nombre.get(),self.edad.get())
		messagebox.showinfo("Alta","Datos registrados :D ")
		self.consultar()

	def consultar(self):
		tabla = ttk.Treeview(self.ventana,columns=("Edad"))
		con = t.Conexion()
		resultado = con.consultar()
		for fila in resultado:
			tabla.insert("",END,text=fila[0],values=(fila[1]))
		tabla.heading("#0",text="Nombre")
		tabla.heading("Edad",text="Edad")
		tabla.place(x=230,y=10)

obj = Interfaz(Tk())
obj.ventana.mainloop()