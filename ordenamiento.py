# Esta función ordena una lista de tareas por fecha_limite usando quicksort
# Se asume que cada elemento de la lista tiene el atributo .fecha_limite

def quicksort_tareas_por_fecha(tareas, izquierda, derecha):
    if izquierda < derecha:
        indice_pivote = particion(tareas, izquierda, derecha)
        quicksort_tareas_por_fecha(tareas, izquierda, indice_pivote - 1)
        quicksort_tareas_por_fecha(tareas, indice_pivote + 1, derecha)


def particion(tareas, izquierda, derecha):
    pivote = tareas[derecha].fecha_limite
    i = izquierda - 1

    for j in range(izquierda, derecha):
        if tareas[j].fecha_limite <= pivote:
            i += 1
            # intercambiar
            tareas[i], tareas[j] = tareas[j], tareas[i]

    tareas[i + 1], tareas[derecha] = tareas[derecha], tareas[i + 1]
    return i + 1