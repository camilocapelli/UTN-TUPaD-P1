# 1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print ("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. 
# Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Por favor, ingresa tu nombre. Para que ejecutemos este TP. ")
print (f"Hola {nombre}.")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. 
# Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. 
# Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla.
nombre = input("Por favor, ingresa tu nombre. Ya sé que te lo pregunté antes pero éste es otro ejercicio. ")
apellido = input(f"Muy bien {nombre}, ahora ingresa tu apellido. ")
edad = input(f"¿Qué edad tienes {nombre}? ")
residencia = input("¿Y cuál es tu país de residencia? ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}. ")

#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.
radio = float(input("Por favor ingresa el radio de un círculo para calcular su area y su perímetro. "))
pi = float(3.1416)
area = round(pi * radio ** 2, 2)
perímetro = round(2 * pi * radio, 2)
print (f"El área del círculo es: {area}, y el perímetro es de: {perímetro}.")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.
segundos = int(input("Por favor, ingresa una cantidad de segundos para ver a cuantas horas equivalen. "))
horas = segundos // 3600
minutos = (segundos % 3600) // 60
segundos_restantes = segundos % 60
print (f"{segundos} segundos equivalen a {horas} horas, {minutos} minutos y {segundos_restantes} segundos. ")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.
número = int(input("Por favor, ingresa un número entero. Veremos su tabla de multiplicar. "))
print(f"La tabla de multiplicar de {número} es:")
print(f"{número} x 1 = {número * 1}")
print(f"{número} x 2 = {número * 2}")
print(f"{número} x 3 = {número * 3}")
print(f"{número} x 4 = {número * 4}")
print(f"{número} x 5 = {número * 5}")
print(f"{número} x 6 = {número * 6}")
print(f"{número} x 7 = {número * 7}")
print(f"{número} x 8 = {número * 8}")
print(f"{número} x 9 = {número * 9}")
print(f"{número} x 10 = {número	* 10}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.
print("Haremos algunas operaciones matemáticas...")
núm1 = int(input("Ingrese un número entero distinto a 0. "))
núm2 = int(input("Por favor ingrese otro número entero distinto a 0. "))
suma = núm1 + núm2
división = round(núm1 / núm2, 2)
multiplicación = núm1 * núm2
resta = núm1 - núm2
print(f"La suma de {núm1} y {núm2} da como resultado {suma}, al dividirlos obtendremos como resultado {división}, la multiplicación da {multiplicación} y la resta da {resta}. ")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.
print("¡Vamos a calcular tu masa corporal!")
altura = float(input("Ingresa tu altura (en metros). "))
peso = float(input("Ingresa tu peso (en kilogramos). "))
IMC = round(peso / (altura) ** 2, 2)
print(f"Tú índice de masa corporal es de {IMC}kg/m². ")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.
print("Vamos a convertir grados Celsiuis en Fahrenheit.")
grados_celsius = float(input("Ingresa la temperatura en °C. "))
grador_fahrenheit = round(float((9/5) * grados_celsius + 32), 2)
print(f"{grados_celsius}°C equivalen a {grador_fahrenheit}°F. ")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.
print("Ingresemos tres números para calcular el promedio. ")
núm1 = float(input())
núm2 = float(input())
núm3 = float(input())
promedio = round((núm1 + núm2 + núm3) / 3 , 2)
print(f"El promedio de los números propocionados es {promedio}. ")

print(f"Llegamos al final del TP, gracias {nombre}!")