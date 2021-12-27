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

	def modificar(self,nombre,edad,nombreM):
		self.conectar()
		cursor = self.conexion.cursor()
		cursor.execute("UPDATE persona SET nombre='"+nombre+"', edad="+str(edad)+" WHERE nombre='"+nombreM+"'")
		self.conexion.commit()
		self.desconectar()

	def eliminar(self,nombre,edad):
		self.conectar()
		cursor = self.conexion.cursor()
		cursor.execute("DELETE FROM persona WHERE nombre='"+nombre+"' AND  edad="+str(edad))
		self.conexion.commit()
		self.desconectar()

	def consultar(self):
		self.conectar()
		cursor = self.conexion.cursor()
		cursor.execute("SELECT nombre,edad FROM persona;")
		resultado = cursor.fetchall()
		self.desconectar()
		return resultado

	def buscar(self,letras):
		self.conectar()
		cursor = self.conexion.cursor()
		cursor.execute("SELECT nombre,edad FROM persona WHERE nombre LIKE '%"+letras+"%';")
		resultado = cursor.fetchall()
		self.desconectar()
		return resultado
