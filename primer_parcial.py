# Inicializamos una lista vacía para almacenar los estudiantes
estudiantes = []

while True:
    # Solicitamos el nombre y matrícula del estudiante
    nombre = input("Ingrese el nombre del estudiante: ")
    matricula = input("Ingrese la matrícula del estudiante: ")

    # Solicitamos las 4 notas del estudiante
    notas = []
    for i in range(1, 5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i}: "))
                if nota < 0:
                    print("No se permiten valores negativos. Intente de nuevo.")
                else:
                    notas.append(nota)
                    break
            except ValueError:
                print("Error: solo se permiten números. Intente de nuevo.")

    # Calculamos el promedio del estudiante
    promedio = sum(notas) / len(notas)

    # Agregamos el estudiante a la lista
    estudiantes.append({"nombre": nombre, "matricula": matricula, "promedio": promedio})

    # Preguntamos si se desea agregar otro estudiante
    respuesta = input("¿Desea agregar otro estudiante? (s/n): ")
    if respuesta.lower() != "s":
        break

# Imprimimos los promedios de cada estudiante
print("Promedios de los estudiantes:")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Matrícula: {estudiante['matricula']}, Promedio: {estudiante['promedio']:.2f}")

# Opción de salida
print("Presione Enter para salir...")
input()
