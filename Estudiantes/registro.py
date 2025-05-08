import csv

def cargarEstudiantes(archivoCsv):

    estudiantesValidos = []

    try:
        with open(archivoCsv, mode='r', encoding='utf-8') as archivo:
            lector = csv.reader(archivo)

            for fila in lector:
                try:

                    nombre = fila[0]
                    notas = [float(nota) for nota in fila[1:]]

                    if all(0.0 <= nota <= 5.0 for nota in notas):
                        estudiantesValidos.append(nombre)
                    else:
                        print(f"Algunas notas están fuera de rango para el estudiante {nombre}: {notas}")

                except ValueError:
                    print(f"Error de conversión en las notas para el estudiante: {fila}")

    except FileNotFoundError:
        print(f"El archivo {archivoCsv} no se encontró.")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

    return estudiantesValidos