## Ejercicio de lista de estudiantes

estudiantes = [
    "Adrián Quintero Pinzón",
    "Alejandra Pinzón Alvarez",
    "Ámbar Isabella Plata López",
    "Andrés David Reyes Espinel",
    "Aura Camila Pico Araque",
    "Camilo Andrés Suárez Fuentes",
    "Daniel Esteban Guerrero Quintero",
    "David Santiago Vera Mendez",
    "Edgar Leonardo Acevedo Arteaga",
    "Gerson Steven Chaparro Martínez",
    "Harley Yefrey Cabrales Vargas",
    "John Stiven Negron Regalado",
    "Juan David Saavedra Jaimez",
    "Juan David Santoyo Jaimes",
    "Juan David Vargas Soto",
    "Juan Eduardo Pinilla Guzmán",
    "Juan Fernando Umaña Barragan",
    "Juan Jose Abril Roman",
    "Maria Juliana Saavedra Mejia",
    "Mateo Roman Camargo",
    "Naya Zarela Lizcano Jaimes",
    "Nicolas Chedraui Mantilla",
    "Omar Fernando Granados Parra",
    "Santiago Aguilar Vesga",
    "Santiago Andrés Quiñonez Sosa",
    "Santiago Jaimes Perez",
    "Sara Sofía Díaz Rodríguez",
    "Sayara Yurley Aparicio Arciniegas",
    "Sergio Andrés Rueda Hernández",
    "Simón Dante Salamanca Galvis",
    "Thomas Sebastián Bastos Garcia",
    "Vladimir Diaz Contreras"
]

def mostrar_estudiantes():
    print("Lista de Estudiantes:")
    for i, estudiante in enumerate(estudiantes, 1):
        print(f"{i}. {estudiante}")

def editar_estudiante():
    mostrar_estudiantes()
    
    try:
        seleccion = int(input("\nSeleccione el número del estudiante que desea editar: "))
        if seleccion < 1 or seleccion > len(estudiantes):
            print("Número inválido. Por favor, seleccione un número dentro del rango.")
            return
        
        estudiante_seleccionado = estudiantes[seleccion - 1]
        print(f"Estudiante seleccionado: {estudiante_seleccionado}")
        
        parte = input("¿Quiere editar el nombre o apellido?: ").lower()

        if parte == "nombre":
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            partes = estudiante_seleccionado.split()
            partes[0] = nuevo_nombre
            estudiantes[seleccion - 1] = " ".join(partes)
            print(f"El nuevo nombre es: {estudiantes[seleccion - 1]}")

        elif parte == "apellido":
            nuevo_apellido = input("Ingrese el nuevo apellido: ")
            partes = estudiante_seleccionado.split()
            partes[1] = nuevo_apellido
            estudiantes[seleccion - 1] = " ".join(partes)
            print(f"El nuevo apellido es: {estudiantes[seleccion - 1]}")

        else:
            print("Opción inválida. Por favor, elija 'nombre' o 'apellido'.")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese un número.")

def importante():
    while True:
        print("\nMenú")
        print("1. Mostrar lista de estudiantes")
        print("2. Editar estudiante")
        print("3. Salir")
        
        opcion = input("Elija una opción: ")

        if opcion == "1":
            mostrar_estudiantes()
        elif opcion == "2":
            editar_estudiante()
        elif opcion == "3":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, elija una opción del 1 al 3.")

# Ejecutar el menú principal
importante()