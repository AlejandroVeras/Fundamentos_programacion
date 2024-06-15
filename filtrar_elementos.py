# Creamos una lista de números
2numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
3
4# Utilizamos una comprensión para filtrar los números pares
5numeros_pares = [n for n in numeros if n % 2 == 0]
6
7print(numeros_pares)  # [2, 4, 6, 8, 10]
