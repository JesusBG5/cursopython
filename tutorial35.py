from tkinter import *
import time

def dibujar():
	for i in range(0,10):
		if i%2 == 0:
			canvas.create_oval(10*i,10*i,200-(i*10),200-(i*10),fill="red")
		else:
			canvas.create_oval(10*i,10*i,200-(i*10),200-(i*10),fill="white")
		time.sleep(1)
		ventana.update()

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Canvas")
canvas = Canvas(ventana,width=500,height=500)
canvas.create_rectangle(0,0,500,500,fill="#76f")
canvas.place(x=0,y=0)
Button(ventana,text="Dibujar",command=dibujar).place(x=200,y=250)
ventana.mainloop()