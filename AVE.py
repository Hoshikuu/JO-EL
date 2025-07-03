vagones = int(input())

for vagon in range(vagones):
    velocidad = 300
    primeraMitad = 0
    segundaMitad = 0
    izquierda = 0
    derecha = 0
    filas = int(input())
    for fila in range(filas):
        datos = input()
        if fila + 1 <= filas // 2:
            derecha += int(datos.split(" ")[0])
            izquierda += int(datos.split(" ")[1])
            primeraMitad += int(datos.split(" ")[0]) + int(datos.split(" ")[1])
            continue
        if filas % 2 == 1:
            if fila + 1 > filas // 2 + 1:
                derecha += int(datos.split(" ")[0])
                izquierda += int(datos.split(" ")[1])
                segundaMitad += int(datos.split(" ")[0]) + int(datos.split(" ")[1])
                continue
            elif fila + 1 == filas // 2 + 1:
                derecha += int(datos.split(" ")[0])
                izquierda += int(datos.split(" ")[1])
                continue
        else:
            if fila + 1 > filas // 2:
                derecha += int(datos.split(" ")[0])
                izquierda += int(datos.split(" ")[1])
                segundaMitad += int(datos.split(" ")[0]) + int(datos.split(" ")[1])
                continue
    velocidad -= (abs(izquierda - derecha) // 50) * 2 + (abs(primeraMitad - segundaMitad) // 100) * 5
    print(velocidad)