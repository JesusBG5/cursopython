#Imprimir los numeros pares 1 100
contador = 1
factorial = 1
n = int(input("Escribe un numero: "))
while contador<=n:
	factorial = factorial * contador
	contador = contador+1
print(factorial)
input()