from tkinter import *

ventana = Tk()
ventana.geometry("500x500")
ventana.title("Canvas")
canvas = Canvas(ventana,width=500,height=500)
#x1,y1, x2,y2
#  rgb   red green blue  #nnn  0-f 0,1,2,3..9,A,B,C,D,E,F
canvas.create_rectangle(0,0,500,500,fill="#76f")
for i in range(0,10):
	if i%2 == 0:
		canvas.create_oval(10*i,10*i,200-(i*10),200-(i*10),fill="red")
	else:
		canvas.create_oval(10*i,10*i,200-(i*10),200-(i*10),fill="white")
canvas.create_oval(350,70,450,170,fill="#F5F5DC")
canvas.create_polygon(400,10,450,90,350,90,fill="yellow")
canvas.create_line(370,110,390,110,width=3.0)
canvas.create_line(415,110,435,110,width=3.0)
canvas.create_line(380,135,425,135,width=3.0)

canvas.place(x=0,y=0)
ventana.mainloop()