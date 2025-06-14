# Práctico – Recursividad
# Programación I - Tecnicatura Universitaria en Programación - UTN
# Alumno: Camilo Capelli
# Comisión: 11

# Ejercicio 1: Factorial recursivo
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

limite = int(input("Ejercicio 1 - Ingresá un número para ver sus factoriales hasta ese número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

# Ejercicio 2: Serie de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

limite = int(input("\nEjercicio 2 - Ingresá hasta qué posición querés ver la serie de Fibonacci: "))
print("Serie de Fibonacci:")
for i in range(limite + 1):
    print(f"f({i}) = {fibonacci(i)}")

# Ejercicio 3: Potencia recursiva
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

b = int(input("\nEjercicio 3 - Base: "))
e = int(input("Exponente: "))
print(f"{b}^{e} = {potencia(b, e)}")

# Ejercicio 4: Decimal a binario recursivo
def decimal_a_binario(n):
    if n == 0:
        return ''
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("\nEjercicio 4 - Ingresá un número decimal para convertirlo a binario: "))
resultado_binario = decimal_a_binario(numero)
print(f"Binario: {resultado_binario if resultado_binario != '' else '0'}")

# Ejercicio 5: Palíndromo recursivo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("\nEjercicio 5 - Ingresá una palabra sin espacios ni tildes: ").lower()
print(f"¿Es palíndromo? {es_palindromo(texto)}")

# Ejercicio 6: Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

numero = int(input("\nEjercicio 6 - Ingresá un número para sumar sus dígitos: "))
print(f"Suma de dígitos: {suma_digitos(numero)}")

# Ejercicio 7: Contar bloques de pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input("\nEjercicio 7 - Ingresá el número de bloques en el nivel más bajo: "))
print(f"Total de bloques necesarios: {contar_bloques(niveles)}")

# Ejercicio 8: Contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

numero = int(input("\nEjercicio 8 - Número: "))
digito = int(input("¿Qué dígito querés contar? (0-9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces.")