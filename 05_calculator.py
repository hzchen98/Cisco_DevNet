# -*- coding: utf-8 -*-
# Ejercicio obligatorio Beca Digitaliza: Programación de redes

# Crear un archivo llamado 05_calculator.py
# Crear las sentencias necesarias para recoger dos números a través del terminal
# Integrar funcionalidades de suma, resta, multiplicación, división, y exponencial
# Implementar funciones, diccionarios, y excepciones
# Permitir escoger el modo de operación de forma manual (el usuario ha de introducir un número para que sepa qué operación realizar)
# Realizar las operaciones e imprimir el valor por pantalla. 

def sumar(a, b):
	return a + b

def restar(a, b):
	return a - b

def multiplicar(a, b):
	return a * b

def dividir(a, b):
	return a / b

def exponencial(a, b):
	total = 1
	while b!=0:
		total *= a
		b -= 1
	return total

def pedirNumero(mensaje, predeterminado):
	numero = "z"
	while not numero.isdigit():
		try:
			numero = input(mensaje)
		except ValueError:
			print("No has instroducido un número correcto, vuelva a intentarlo!(Pulse exit para salir)")
			if numero=="exit":
				return predeterminado
	return int(numero)

def imprimirFunctionDic(diccionario, mensaje):
	print(mensaje)
	for i, j in diccionario.items():
		print(i, j.__name__, sep="-")

def pedirNumeroRango(mensaje, predeterminado, minimo, maximo):
	numero = pedirNumero(mensaje, predeterminado)
	while numero > maximo or numero < minimo:
		print("\nDebe de introducir un número entre", minimo, "y", maximo)
		numero = pedirNumero(mensaje, predeterminado)
	return numero


VALOR_PREDETERMINADO = "nada"
OPERACIONES = {1:sumar, 2:restar, 3:multiplicar, 4:dividir, 5:exponencial}

print("Ejercicio obligatorio Beca Digitaliza: Programación de redes - Calculadora\n")

num1 = pedirNumero("Primer número:", VALOR_PREDETERMINADO)

if not num1 == VALOR_PREDETERMINADO:
	num2 = pedirNumero("Segundo número:", VALOR_PREDETERMINADO)

	if not num2 == VALOR_PREDETERMINADO:
		imprimirFunctionDic(OPERACIONES, "\nMenú de cálculos:")
		accion = pedirNumeroRango("¿Qué cálculo desea realizar?:", VALOR_PREDETERMINADO, min(OPERACIONES.keys()), max(OPERACIONES.keys()))

		try:
			print("El resultado es",OPERACIONES[accion](num1, num2))
		except ZeroDivisionError as e:
			print("División errónea, el divisor no puede ser 0!")