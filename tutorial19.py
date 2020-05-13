class Electrodomestico:

	def __init__(self):
		self.encendido = False

	def encender(self):
		self.encendido = True
		print("El aparato se encendió")

	def apagar(self):
		self.encendido = False
		print("El aparato se apagó ")

	def comprobar(self):
		if(self.encendido == True):
			print("El aparato está encendido ")
		else:
			print("El aparato está apagado ")

class Celular(Electrodomestico):

	def instalarAplicacion(self,nombre):
		print(nombre + " se está instalando")

class Television(Electrodomestico):

	def cambiarCanal(self,canal):
		print("La televisión cambio al canal : " + str(canal))

tele = Television()
cel = Celular()
tele.encender()
tele.comprobar()
cel.apagar()
cel.comprobar()
cel.instalarAplicacion("Facebook")