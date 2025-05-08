# tallerGit
Desarrollar una aplicación en Python que lea estudiantes desde un archivo CSV, los procese, imprima una tabla y calcule el promedio, trabajando exclusivamente sobre la rama main. Se deben hacer commits pequeños y frecuentes, y configurar un pipeline CI (GitHub Actions) para ejecutar automáticamente el programa y validar su formato.

Commits:

El primer commit debe consistir en la creación del archivo estudiantes.csv con datos de prueba. Este archivo debe contener al menos cinco estudiantes, cada uno con su respectiva nota, y servirá como entrada para el programa. El mensaje sugerido para este commit es: "Crear archivo estudiantes.csv con datos de prueba".

El segundo commit corresponde a la estructura base del proyecto. En esta etapa, se debe crear el archivo main.py como punto de entrada del programa, así como la carpeta estudiantes/ con un archivo llamado registro.py, que contendrá las funciones de procesamiento. El mensaje sugerido para este commit es: "Crear estructura base del proyecto".

El tercer commit debe implementar la función que carga los estudiantes desde el archivo CSV. Esta función debe leer los datos, validar que las notas estén en un rango válido (entre 0.0 y 5.0) y devolver una lista de estudiantes válidos. El mensaje del commit puede ser: "Implementar carga de estudiantes desde CSV con validación".

En el cuarto commit, se debe crear la función que ordena a los estudiantes alfabéticamente y los imprime en formato tabular, con columnas bien alineadas para nombre y nota. Esta función debe permitir visualizar claramente la información procesada. El mensaje sugerido es: "Mostrar estudiantes ordenados en formato de tabla".

El quinto commit está dedicado a calcular el promedio general de las notas. Se debe implementar una función que recorra la lista de estudiantes válidos y calcule la media de sus notas, mostrando el resultado con dos decimales. El mensaje para este cambio debe ser: "Calcular y mostrar promedio general de notas".

El sexto commit debe integrar todo el flujo de ejecución dentro de main.py, enlazando las funciones previamente desarrolladas. Al ejecutar el archivo, el programa debe cargar los datos desde el CSV, mostrar la tabla de estudiantes y calcular el promedio. El mensaje del commit puede ser: "Integrar flujo completo de ejecución en main.py".

Finalmente, el séptimo commit corresponde a la configuración del pipeline de integración continua. En esta etapa, se debe crear un archivo en .github/workflows/ci.yml que automatice la ejecución del programa. Este pipeline debe ejecutarse en cada push realizado sobre la rama main. El mensaje de este commit debe ser: "Configurar pipeline CI para ejecutar y validar la aplicación".