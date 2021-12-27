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
		Button(ventana,command=self.eliminar,text="Eliminar").place(x=270,y=250)
		self.consultar()

	def guardar(self):
		con = t.Conexion()
		con.insertar(self.nombre.get(),self.edad.get())
		messagebox.showinfo("Alta","Datos registrados :D ")
		self.consultar()

	def eliminar(self):
		fila = self.tabla.focus()
		#print(self.tabla.item(fila))
		#print(self.tabla.item(fila)["text"])
		#print(self.tabla.item(fila)["values"][0])
		op=messagebox.askquestion("¿Eliminar?","¿Estás seguro de eliminar ese contacto?")
		#print(op)
		nombre = self.tabla.item(fila)["text"]
		edad = self.tabla.item(fila)["values"][0]
		if op=="yes":
			con = t.Conexion()
			con.eliminar(nombre,edad)
		self.consultar()

	def consultar(self):
		self.tabla = ttk.Treeview(self.ventana,columns=("Edad"))
		con = t.Conexion()
		resultado = con.consultar()
		for fila in resultado:
			self.tabla.insert("",END,text=fila[0],values=(fila[1]))
		self.tabla.heading("#0",text="Nombre")
		self.tabla.heading("Edad",text="Edad")
		self.tabla.place(x=230,y=10)

obj = Interfaz(Tk())
obj.ventana.mainloop()