import mysql.connector
from mysql.connector import errorcode

class Conexion:

	def conectar(self):
		try:
			self.conexion = mysql.connector.connect(user='root',
				password='',
				host='localhost',
				database='python')
			print("Conectado correctamente")
		except mysql.connector.Error as err:
			if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
				print("Error de usuario o contraseña")
			elif err.errno == errorcode.ER_BAD_DB_ERROR:
				print("Base de datos no existe")
			else:
				print(err)

	def desconectar(self):
		print("Cerrando conexión...")
		self.conexion.close()
		print("Conexion cerrada")

	def insertar(self,nombre,edad):
		self.conectar()
		cursor = self.conexion.cursor()
		cursor.execute("INSERT INTO persona VALUES (null,'"+nombre+"',"+str(edad)+")")
		self.conexion.commit()
		self.desconectar()