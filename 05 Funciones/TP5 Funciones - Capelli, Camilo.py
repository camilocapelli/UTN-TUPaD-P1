# Práctico 2 – Funciones en Python
# Programación I - Tecnicatura Universitaria en Programación - UTN
# Alumno: Camilo Capelli
# Comisión: 11

import math

# 1. imprimir_hola_mundo
def imprimir_hola_mundo():
    print("Hola Mundo!\n")

imprimir_hola_mundo()


# 2. saludar_usuario(nombre)
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

nombre_usuario = input("Ingresá tu nombre: ")
print(saludar_usuario(nombre_usuario))


# 3. informacion_personal(nombre, apellido, edad, residencia)
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

nombre = input("\nNombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
residencia = input("Lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia)


# 4. calcular_area_circulo(radio) y calcular_perimetro_circulo(radio)
def calcular_area_circulo(radio):
    return math.pi * (radio)**2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("\nIngresá el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"Área: {round(area, 2)}")
print(f"Perímetro: {round(perimetro, 2)}")


# 5. segundos_a_horas(segundos)
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("\nIngresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"Equivale a {round(horas, 2)} horas.")


# 6. tabla_multiplicar(numero)
def tabla_multiplicar(numero):
    print(f"Tabla del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("\nIngresá un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)


# 7. operaciones_basicas(a, b)
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    producto = a * b
    division = a / b if b != 0 else "Infinito (no se puede dividir por cero)"
    return (suma, resta, producto, division)

a = float(input("\nPrimer número: "))
b = float(input("Segundo número: "))
resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {round(resultados[3], 2)}")


# 8. calcular_imc(peso, altura)
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("\nIngresá tu peso en kg: "))
altura = float(input("Ingresá tu altura en metros: "))
imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {round(imc, 2)}")


# 9. celsius_a_fahrenheit(celsius)
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("\nIngresá la temperatura en °C: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius}°C equivalen a {round(fahrenheit, 2)}°F")


# 10. calcular_promedio(a, b, c)
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

n1 = float(input("\nPrimer número para el promedio: "))
n2 = float(input("Segundo número: "))
n3 = float(input("Tercer número: "))
promedio = calcular_promedio(n1, n2, n3)
print(f"El promedio es: {round(promedio, 2)}")
