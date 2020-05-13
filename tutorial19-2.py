class Persona:

	def __init__(self,n,app,apm,num):
		self.nombre = n 
		self.app = app
		self.apm = apm
		self.dia = num

	def generarCorreo(self):
		self.correo = self.nombre + self.app[0] + self.apm[0] + str(self.dia) + "@upvt.edu.mx"

	def imprimir(self):
		print("Nombre: " + self.nombre + " " + self.app + " " + self.apm)
		print("Día de nacimiento : " + str(self.dia))
		print("Correo : " + self.correo)

class Alumno(Persona):

	def __init__(self,n,app,apm,num,m):
		self.matricula = m
		Persona.__init__(self,n,app,apm,num)

	def imprimirAlumno(self):
		self.imprimir()
		print("Matricula : " + self.matricula)

class Maestro(Persona):

	def __init__(self,n,app,apm,num,ne,t):
		self.numEmp = ne
		self.titulo = t
		Persona.__init__(self,n,app,apm,num)

	def imprimirMaestro(self):
		self.imprimir()
		print("EL numero de empleado es: " + str(self.numEmp))
		print("El titulo es: " + self.titulo)

alu1 = Alumno("Ivan","Alba","Miranda","24","1218INI078")
mae1 = Maestro("Jesus","Becerril","Gutierrez",28,701,"Maestro en Administracion")
alu1.generarCorreo()
mae1.generarCorreo()
alu1.imprimirAlumno()
print("*****************")
mae1.imprimirMaestro()