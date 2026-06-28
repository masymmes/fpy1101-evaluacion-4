def validar_titulo(titulo):
    if titulo.strip() == "":
        return False
    return True


def validar_copias(copias):
    try:
        numero = int(copias)
        if numero >= 0:
            return True
        return False
    except:
        return False


def validar_prestamo(prestamo):
    try:
        numero = int(prestamo)
        if numero > 0:
            return True
        return False
    except:
        return False


def mostrar_menu():
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Agregar libro")
    print("2. Buscar libro")
    print("3. Eliminar libro")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar libros")
    print("6. Salir")
    print("=====================================")


def leer_opcion():
    while True:
        opcion = input("Ingrese opcion: ")
        try:
            opcion = int(opcion)
            if opcion >= 1 and opcion <= 6:
                return opcion
            else:
                print("Opcion no valida, ingrese un numero entre 1 y 6")
        except:
            print("Opcion no valida, ingrese un numero entre 1 y 6")


def agregar_libro(libros):
    titulo = input("Titulo del libro: ")
    copias = input("Cantidad de copias: ")
    prestamo = input("Dias de prestamo: ")

    ok_titulo = validar_titulo(titulo)
    ok_copias = validar_copias(copias)
    ok_prestamo = validar_prestamo(prestamo)

    if ok_titulo == False:
        print("Error: el titulo no puede estar vacio")
    if ok_copias == False:
        print("Error: las copias deben ser un numero entero mayor o igual a cero")
    if ok_prestamo == False:
        print("Error: el prestamo debe ser un numero entero mayor que cero")

    if ok_titulo == True and ok_copias == True and ok_prestamo == True:
        libro = {
            "titulo": titulo.strip(),
            "copias": int(copias),
            "prestamo": int(prestamo),
            "disponible": False
        }
        libros.append(libro)
        print("Libro agregado con exito")


def buscar_libro(libros, titulo):
    for i in range(len(libros)):
        if libros[i]["titulo"] == titulo:
            return i
    return -1


def eliminar_libro(libros):
    titulo = input("Titulo del libro a eliminar: ")
    pos = buscar_libro(libros, titulo)
    if pos != -1:
        libros.pop(pos)
        print("Libro eliminado")
    else:
        print("El libro '" + titulo + "' no se encuentra registrado.")


def actualizar_disponibilidad(libros):
    for i in range(len(libros)):
        if libros[i]["copias"] >= 1:
            libros[i]["disponible"] = True
        else:
            libros[i]["disponible"] = False


def mostrar_libros(libros):
    actualizar_disponibilidad(libros)
    print("\n=== LISTA DE LIBROS ===")
    if len(libros) == 0:
        print("No hay libros registrados")
    else:
        for libro in libros:
            if libro["disponible"] == True:
                estado = "DISPONIBLE"
            else:
                estado = "SIN COPIAS"
            print("Título: " + libro["titulo"])
            print("Copias: " + str(libro["copias"]))
            print("Préstamo: " + str(libro["prestamo"]))
            print("Estado: " + estado)
            print("*" * 45)


def main():
    libros = []

    while True:
        mostrar_menu()
        opcion = leer_opcion()

        if opcion == 1:
            agregar_libro(libros)

        elif opcion == 2:
            titulo = input("Ingrese titulo a buscar: ")
            pos = buscar_libro(libros, titulo)
            if pos != -1:
                libro = libros[pos]
                if libro["disponible"] == True:
                    estado = "DISPONIBLE"
                else:
                    estado = "SIN COPIAS"
                print("Libro encontrado en posicion " + str(pos))
                print("Título: " + libro["titulo"])
                print("Copias: " + str(libro["copias"]))
                print("Préstamo: " + str(libro["prestamo"]))
                print("Estado: " + estado)
            else:
                print("El libro '" + titulo + "' no se encuentra registrado.")

        elif opcion == 3:
            eliminar_libro(libros)

        elif opcion == 4:
            actualizar_disponibilidad(libros)
            print("Disponibilidad actualizada")

        elif opcion == 5:
            mostrar_libros(libros)

        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
            break


main()
