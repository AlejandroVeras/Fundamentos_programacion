#calculadora de indice de masa corporal

peso = float(input("Ingrese su peso en Kilogramos: "))
estatura = float(input("Ingrese su estatura en metros: "))

masa_corporal = round(peso / (estatura ** 2), 1)

print("Su indice de masa corporal es de", masa_corporal)
