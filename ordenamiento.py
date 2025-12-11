# Esta función ordena una lista de tareas por fecha_limite usando quicksort
# Se asume que cada elemento de la lista tiene el atributo .fecha_limite

# Función principal del algoritmo Quicksort (recursiva)
def quicksort_tareas_por_fecha(tareas, izquierda, derecha):
    # La condición base para la recursividad: solo si el subarreglo tiene 2 o más elementos
    if izquierda < derecha:
        # Llama a la función de partición para seleccionar un pivote y reordenar el subarreglo
        indice_pivote = particion(tareas, izquierda, derecha)
         # Llama recursivamente a quicksort para el subarreglo de elementos menores que el pivote
        quicksort_tareas_por_fecha(tareas, izquierda, indice_pivote - 1)
        # Llama recursivamente a quicksort para el subarreglo de elementos mayores que el pivote
        quicksort_tareas_por_fecha(tareas, indice_pivote + 1, derecha)


# Función que realiza la partición (reordenamiento) de un subarreglo alrededor de un pivote
def particion(tareas, izquierda, derecha):
    # Selecciona el último elemento del subarreglo como pivote, basándose en su fecha_limite
    pivote = tareas[derecha].fecha_limite
    # Inicializa el índice del elemento más pequeño (i), que actuará como marcador para la posición final del pivote
    i = izquierda - 1

     # Itera sobre los elementos del subarreglo (desde 'izquierda' hasta 'derecha' - 1)
    for j in range(izquierda, derecha):
         # Compara la fecha límite de la tarea actual (tareas[j]) con la del pivote
        if tareas[j].fecha_limite <= pivote:
            i += 1
            # Si el elemento es menor o igual al pivote, se intercambia con tareas[i] 
            # (colocándolo en la sección de 'menores que el pivote')
            tareas[i], tareas[j] = tareas[j], tareas[i]

    # Coloca el pivote en su posición correcta, separando los elementos menores y mayores.
    # Intercambia el pivote (tareas[derecha]) con el elemento justo después de la sección de menores (tareas[i + 1])
    tareas[i + 1], tareas[derecha] = tareas[derecha], tareas[i + 1]
    # Retorna la posición final donde quedó el pivote
    return i + 1
