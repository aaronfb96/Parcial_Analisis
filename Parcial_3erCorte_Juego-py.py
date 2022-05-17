import random
 
intentos = 0
 
print("Hola. Jugaremos 'Adivina el numero'. ¿Cómo te llamas?:", end=" ")
nombre = input()
 
numero = random.randint(1, 10)
print("Hola " + nombre + ". Estoy pensando un numero entre el 1 y el 10.")
print("")
 
while intentos < 3:
	print("¿Que numero estoy pensando?: ", end=" ")
	adivina = input()
	try:
		adivina = int(adivina)
	except:
		print("Debes ingresar un valor numerico.")
		# Si no define un numero, se reinicia el bucle
		continue
 
	# Aumentamos el contador
	intentos = intentos + 1
 
	if adivina < numero:
		print("El numero a adivinar debe ser mayor. ") 
 
	if adivina > numero:
		print("El numero a adivinar debe ser menor. ")
 
	if adivina == numero:
		break
 
if adivina == numero:
	intentos = str(intentos)
	print("Bien " + nombre + ". has adivinado el numero en " + intentos + " intentos!")
 
if adivina != numero:
	numero = str(numero)
	print("No adivinaste el numero. El numero era " + numero)