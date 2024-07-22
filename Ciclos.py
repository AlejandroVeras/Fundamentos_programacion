#Ejercicio 1 Leer un número entero y mostrar todos los enteros comprendidos entre 1 y el número leído.

numero = int(input("Introduce un número entero: "))
for i in range(1, numero + 1):
    print(i)

#Ejercicio 2 Leer un número entero y mostrar todos los pares comprendidos entre 1 y el número leído.

numero = int(input("Introduce un número entero: "))
for i in range(1, numero + 1):
    if i % 2 == 0:
        print(i)

# Ejercicio 3 Leer un número entero y mostrar todos los divisores exactos del número comprendidos entre 1 y el número leído.

numero = int(input("Introduce un número entero: "))
for i in range(1, numero + 1):
    if numero % i == 0:
        print(i)

#Ejercicio 4 Leer dos números y mostrar todos los enteros comprendidos entre ellos.

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
for i in range(numero1, numero2 + 1):
    print(i)

#Ejercicio 5 Leer dos números y mostrar todos los números terminados en 4 comprendidos entre ellos.

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
for i in range(numero1, numero2 + 1):
    if i % 10 == 4:
        print(i)

#Ejercicio 6 Leer un número entero de tres dígitos y mostrar todos los enteros comprendidos entre 1 y cada uno de los dígitos.

numero = int(input("Introduce un número entero de tres dígitos: "))
cientos = numero // 100
decenas = (numero // 10) % 10
unidades = numero % 10
for i in range(1, cientos + 1):
    print(i)
for i in range(1, decenas + 1):
    print(i)
for i in range(1, unidades + 1):
    print(i)

#Ejercicio 7 Mostrar en pantalla todos los enteros comprendidos entre 1 y 100.

for i in range(1, 101):
    print(i)

#Ejercicio 8 Mostrar en pantalla todos los pares comprendidos entre 20 y 200.

for i in range(20, 201):
    if i % 2 == 0:
        print(i)

#Ejercicio 9 Mostrar en pantalla todos los números terminados en 6 comprendidos entre 25 y 205.

for i in range(25, 206):
    if i % 10 == 6:
        print(i)

#Ejercicio 10 Leer un número entero y determinar a cuánto es igual la suma de todos los enteros comprendidos entre 1 y el número leído.

numero = int(input("Introduce un número entero: "))
suma = sum(range(1, numero + 1))
print(suma)

#Ejercicio 11 Leer un número entero de dos dígitos y mostrar en pantalla todos los enteros comprendidos entre un dígito y otro.

numero = int(input("Introduce un número entero de dos dígitos: "))
decenas = numero // 10
unidades = numero % 10
for i in range(decenas, unidades + 1):
    print(i)

#Ejercicio 12 Leer un número entero de 3 dígitos y determinar si tiene el dígito 1.

numero = int(input("Introduce un número entero de tres dígitos: "))
if '1' in str(numero):
    print("El número tiene el dígito 1.")
else:
    print("El número no tiene el dígito 1.")

#Ejercicio 13 Leer un entero y mostrar todos los múltiplos de 5 comprendidos entre 1 y el número leído.

numero = int(input("Introduce un número entero: "))
for i in range(1, numero + 1):
    if i % 5 == 0:
        print(i)

#Ejercicio 14 Mostrar en pantalla los primeros 20 múltiplos de 3.

for i in range(1, 21):
    print(i * 3)

#Ejercicio 15 Escribir en pantalla el resultado de sumar los primeros 20 múltiplos de 3.

suma = sum(i * 3 for i in range(1, 21))
print(suma)

#Ejercicio 16 Promediar los x primeros múltiplos de 2 y determinar si ese promedio es mayor que los y primeros múltiplos de 5 para valores de x y y leídos.

x = int(input("Introduce el valor de x: "))
y = int(input("Introduce el valor de y: "))
promedio_multiplos_2 = sum(i * 2 for i in range(1, x + 1)) / x
promedio_multiplos_5 = sum(i * 5 for i in range(1, y + 1)) / y
if promedio_multiplos_2 > promedio_multiplos_5:
    print("El promedio de los primeros", x, "múltiplos de 2 es mayor.")
else:
    print("El promedio de los primeros", y, "múltiplos de 5 es mayor.")

#Ejercicio 17 Leer números hasta que digiten 0 y determinar a cuánto es igual el promedio de los números terminados en 5.

numeros = []
while True:
    numero = int(input("Introduce un número (0 para terminar): "))
    if numero == 0:
        break
    if numero % 10 == 5:
        numeros.append(numero)
if numeros:
    promedio = sum(numeros) / len(numeros)
    print("El promedio de los números terminados en 5 es:", promedio)
else:
    print("No se ingresaron números terminados en 5.")

#Ejercicio 18 Generar los números del 1 al 10 utilizando un ciclo que vaya de 10 a 1.

for i in range(10, 0, -1):
    print(11 - i)

#Ejercicio 19 Leer un número entero y mostrar en pantalla su tabla de multiplicar.

numero = int(input("Introduce un número entero: "))
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)

#Ejercicio 20 Leer un número entero y calcular a cuánto es igual la sumatoria de todas las factoriales de los números comprendidos entre 1 y el número leído.

n = int(input("Introduce un número entero:"))
sumatoria = 0
for i in range(1, n+1):
    factorial = 1
    for j in range(1, i+1):
        factorial *= j
    sumatoria += factorial
print("La suma de los factoriales es:", sumatoria)
