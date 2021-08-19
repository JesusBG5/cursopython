from tkinter import *
from tkinter import messagebox

class Ventana:

	def __init__(self,inter):
		self.interfaz = inter
		self.interfaz.geometry("300x300")
		self.interfaz.title("Tkinter y POO")
		self.num1 = IntVar()
		self.num2 = IntVar()
		self.dibujarVentana()

	def dibujarVentana(self):
		Label(self.interfaz,text="Escribe un número: ").place(x=10,y=10)
		Entry(self.interfaz,textvariable=self.num1).place(x=20,y=30)
		Entry(self.interfaz,textvariable=self.num2).place(x=20,y=80)
		Button(self.interfaz,command=self.sumar,text="Sumar").place(x=50,y=110)

	def sumar(self):
		res = self.num1.get()+self.num2.get()
		messagebox.showinfo("Resultado","El resultado es: "+str(res))

obj = Ventana(Tk())
obj.interfaz.mainloop()