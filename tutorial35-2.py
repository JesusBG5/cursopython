from tkinter import *
from tkinter import ttk

def dibujar():
	canvas.create_polygon(400,10,450,90,350,90,fill=color.get())

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Canvas")
canvas = Canvas(ventana,width=500,height=500)
canvas.create_rectangle(0,0,500,500,fill="#76f")
canvas.create_oval(350,70,450,170,fill="#F5F5DC")
canvas.create_polygon(400,10,450,90,350,90,fill="yellow")
canvas.create_line(370,110,390,110,width=3.0)
canvas.create_line(415,110,435,110,width=3.0)
canvas.create_line(380,135,425,135,width=3.0)
color = StringVar()
colores = ("Yellow","Blue","Red","Green","Black","Brown","Gray","Orange")
combo = ttk.Combobox(ventana,state="readonly",textvariable=color)
combo.place(x=200,y=210)
combo["values"] = colores
Button(ventana,text="Dibujar",command=dibujar).place(x=200,y=250)

canvas.place(x=0,y=0)
ventana.mainloop()