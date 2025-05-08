from Estudiantes.registro import cargarEstudiantes

archivoEstudiantes = 'estudiantes.csv'
estudiantes = cargarEstudiantes(archivoEstudiantes)

print("Estudiantes válidos:")
for estudiante in estudiantes:
    print(estudiante)