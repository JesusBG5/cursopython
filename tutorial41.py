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
		self.letras = StringVar()
		# Guardar para modificar=1  Guardar para agregar=0
		self.guardarM = 0 
		# Guardar el nombre a modificar
		self.nombreM = ""
		Label(ventana,text="Nombre: ").place(x=5,y=10)
		Entry(ventana,textvariable=self.nombre).place(x=70,y=10)
		Label(ventana,text="Edad: ").place(x=5,y=80)
		Entry(ventana,textvariable=self.edad).place(x=70,y=80)
		self.botonPrincipal = Button(ventana,command=self.guardar,text="Guardar")
		self.botonPrincipal.place(x=70,y=150)
		Button(ventana,command=self.eliminar,text="Eliminar").place(x=270,y=300)
		Button(ventana,command=self.cargar,text="Modificar").place(x=370,y=300)
		Label(ventana,text="Buscar: ").place(x=270,y=10)
		busqueda = Entry(ventana,textvariable=self.letras)
		busqueda.place(x=320,y=10)
		busqueda.bind("<KeyRelease>",self.busqueda)
		self.consultar()

	def guardar(self):
		if self.guardarM==0:
			con = t.Conexion()
			con.insertar(self.nombre.get(),self.edad.get())
			messagebox.showinfo("Alta","Datos registrados :D ")
		else:
			con = t.Conexion()
			con.modificar(self.nombre.get(),self.edad.get(),self.nombreM)
			messagebox.showinfo("Modificar","Datos modificados :D ")
		self.consultar()
		self.limpiar()

	def limpiar(self):
		self.nombre.set("")
		self.edad.set(0)
		self.guardarM = 0
		self.nombreM = ""
		self.botonPrincipal.configure(text="Guardar")

	def eliminar(self):
		fila = self.tabla.focus()
		if len(str(fila))>0:
			op=messagebox.askquestion("¿Eliminar?","¿Estás seguro de eliminar ese contacto?")
			nombre = self.tabla.item(fila)["text"]
			edad = self.tabla.item(fila)["values"][0]
			if op=="yes":
				con = t.Conexion()
				con.eliminar(nombre,edad)
			self.consultar()
		else:
			messagebox.showinfo("Aviso","No seleccionaste ninguna fila")

	def cargar(self):
		fila = self.tabla.focus()
		if len(str(fila))>0:
			nombre = self.tabla.item(fila)["text"]
			edad = self.tabla.item(fila)["values"][0]
			self.nombre.set(nombre)
			self.edad.set(edad)
			self.guardarM = 1
			self.nombreM = nombre
			self.botonPrincipal.configure(text="Guardar cambios")
		else:
			messagebox.showinfo("Aviso","No seleccionaste ninguna fila")

	def consultar(self):
		self.tabla = ttk.Treeview(self.ventana,columns=("Edad"))
		con = t.Conexion()
		resultado = con.consultar()
		for fila in resultado:
			self.tabla.insert("",END,text=fila[0],values=(fila[1]))
		self.tabla.heading("#0",text="Nombre")
		self.tabla.heading("Edad",text="Edad")
		self.tabla.place(x=230,y=60)

	def busqueda(self,key):
		self.tabla = ttk.Treeview(self.ventana,columns=("Edad"))
		con = t.Conexion()
		resultado = con.buscar(self.letras.get())
		for fila in resultado:
			self.tabla.insert("",END,text=fila[0],values=(fila[1]))
		self.tabla.heading("#0",text="Nombre")
		self.tabla.heading("Edad",text="Edad")
		self.tabla.place(x=230,y=60)
		#print(self.letras.get())

obj = Interfaz(Tk())
obj.ventana.mainloop()