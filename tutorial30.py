from tkinter import *
from tkinter import ttk

ventana = Tk()
ventana.geometry("600x500")
ventana.title("Treeview")

arbol = ttk.Treeview(ventana,columns=("Precio","Cantidad"))
arbol.insert("",END,text="Principe",values=("10","15"))
arbol.insert("",END,text="Papas",values=("12","7"))
arbol.heading("#0",text="Nombre")
arbol.heading("Precio",text="Precio")
arbol.heading("Cantidad",text="Cantidad")
'''
menu1 = arbol.insert("",END,text="Menú 1")
menu2 = arbol.insert("",END,text="Menú 2")
arbol.insert(menu1,END,text="Elemento 1")
arbol.insert(menu1,END,text="Elemento 2")
arbol.insert(menu1,END,text="Elemento 3")
arbol.insert(menu2,END,text="Elemento 1")
'''
arbol.place(x=10,y=10)

#print(arbol.get_children(menu2))

ventana.mainloop()