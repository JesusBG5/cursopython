while True:
	try:
		a = int(input("Escribe un número: "))
		b = int(input("Escribe otro número: "))
		res = a/b
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
	except ValueError:
		print("Solo se aceptan números")
	else:
		print("El resultado: ",res)
	finally: 
		print("Esta es una prueba")
	input()