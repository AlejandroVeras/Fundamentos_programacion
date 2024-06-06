# Leer dos números enteros
numero1 = int(input("Ingrese el primer número: "))
numero2 = int(input("Ingrese el segundo número: "))

# Calcular la diferencia entre los dos números
diferencia = abs(numero1 - numero2)

# Verificar si la diferencia es par
if diferencia % 2 == 0:
    # Calcular la suma de los dígitos de los números
    suma_digitos = sum(int(digito) for digito in str(numero1) + str(numero2))
    print("La suma de los dígitos es:", suma_digitos)

# Verificar si la diferencia es un número primo menor que 10
elif diferencia in [2, 3, 5, 7]:
    # Calcular el producto de los dos números
    producto = numero1 * numero2
    print("El producto de los números es:", producto)

# Verificar si la diferencia termina en 4
elif str(diferencia)[-1] == '4':
    # Mostrar todos los dígitos por separado
    for digito in str(numero1) + str(numero2):
        print(digito)
