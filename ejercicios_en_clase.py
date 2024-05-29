#Iteracion sobre la lista de nombres que imprima solamente los nombres que tengan igual o mas de tres vocales.

vocales = ["a","e","i","o","u"]
nombres = input("Ingrese el nombre:")
numero_vocales = 0

for item in list(nombres):
  if item in vocales:
    numero_vocales += 1

if numero_vocales>=3:
  print(nombres)
else:
  print("No hay nombres con 3 o mas vocales")
