estudiantes = []

while True:
    nombre = input("Ingrese el nombre del estudiante: ")
    matricula = input("Ingrese la matrícula del estudiante: ")
    carrera = input("Ingrese la carrera del estudiante: ")
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

  
    promedio = sum(notas) / len(notas)


    estudiantes.append({"nombre": nombre, "matricula": matricula, "carrera": carrera, "promedio": promedio})


    respuesta = input("¿Desea agregar otro estudiante? (s/n): ")
    if respuesta.lower() != "s":
        break


print("Promedios de los estudiantes:")
for estudiante in estudiantes:
    print(f"Nombre: {estudiante['nombre']}, Matrícula: {estudiante['matricula']}, Carrera: {estudiante['carrera']}, Promedio: {estudiante['promedio']:.2f}")


print("Presione Enter para salir...")
input()
