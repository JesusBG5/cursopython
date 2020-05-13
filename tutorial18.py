#Clases y Objetos
class Celular:

	def __init__(self,t,s):
		self.tam = t 
		self.sistema = s
		self.espacio = t

	def instalar(self,nombre,peso):
		if self.espacio>=peso:
			print(nombre+" instalad@")
			self.espacio = self.espacio - peso
		else:
			print("Espacio insuficiente")

obj = Celular(1000,"Android")
obj.instalar("Facebook",200)
obj.instalar("Instagram",300)
obj.instalar("Uber",300)
obj.instalar("Youtube",300)

input()