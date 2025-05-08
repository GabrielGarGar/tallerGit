import csv

def cargarEstudiantes(archivo_csv):
    """
    Carga los datos de los estudiantes desde un archivo CSV sin encabezados,
    validando que las notas estén entre 0.0 y 5.0.

    :param archivo_csv: Ruta del archivo CSV que contiene los datos de los estudiantes.
    :return: Lista de diccionarios con 'Nombre' y 'Promedio' de los estudiantes válidos.
    """
    estudiantes_validos = []

    try:
        with open(archivo_csv, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)

            for fila in lector:
                try:
                    # El primer campo es el nombre, el resto son las notas
                    nombre = fila[0]
                    notas = [float(nota) for nota in fila[1:]]  # Convertir las notas a flotantes

                    # Validar que todas las notas estén en el rango válido
                    notas_validas = [nota for nota in notas if 0.0 <= nota <= 5.0]

                    if len(notas_validas) == len(notas):
                        promedio = sum(notas_validas) / len(notas_validas)
                        estudiantes_validos.append({'Nombre': nombre, 'Promedio': promedio})
                    else:
                        print(f"Algunas notas están fuera de rango para el estudiante {nombre}: {notas}")
                except ValueError:
                    print(f"Error de conversión en las notas para el estudiante: {fila}")
    except FileNotFoundError:
        print(f"El archivo {archivo_csv} no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    print("Nombres de estudiantes válidos:")
    for estudiante in estudiantes_validos:
        print(estudiante['Nombre'])

    return estudiantes_validos




def mostrar_estudiantes_ordenados(estudiantes):
    """
    Ordena a los estudiantes alfabéticamente por nombre y los imprime en formato tabular.

    :param estudiantes: Lista de diccionarios con los datos de los estudiantes.
    Cada diccionario debe tener las claves 'Nombre' y 'Promedio'.
    """
    # Ordenar la lista de estudiantes por nombre
    estudiantes_ordenados = sorted(estudiantes, key=lambda estudiante: estudiante['Nombre'])

    # Imprimir los encabezados de la tabla
    print(f"{'Nombre'.ljust(30)}{'Promedio':>10}")
    print("-" * 40)

    # Imprimir cada estudiante en formato tabular
    for estudiante in estudiantes_ordenados:
        nombre = estudiante['Nombre']
        promedio = f"{estudiante['Promedio']:.2f}"  # Formatear el promedio a 2 decimales
        print(f"{nombre.ljust(30)}{promedio:>10}")