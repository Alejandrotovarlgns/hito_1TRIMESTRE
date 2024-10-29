def main():
    # Solicitar el saldo inicial
    while True:
        try:
            # Pedimos al usuario que ingrese el saldo inicial
            saldo = float(input("Ingrese el saldo inicial de la cuenta: "))
            # Verificamos que el saldo no sea negativo
            if saldo < 0:
                print("El saldo no puede ser negativo. Intente nuevamente.")
            else:
                break  # Si el saldo es válido, salimos del bucle
        except ValueError:
            # Capturamos el error si la entrada no es un número válido
            print("Por favor, ingrese un número válido.")

    # Inicializamos contadores para ingresos y retiradas
    ingresos = 0
    retiradas = 0

    while True:
        # Mostrar el menú de opciones
        print("\nMenú:")
        print("1 - Ingresar dinero")
        print("2 - Retirar dinero")
        print("3 - Mostrar saldo")
        print("4 - Estadísticas")
        print("5 - Salir")

        # Solicitar la opción del menú al usuario
        while True:
            try:
                # Pedimos una opción y la convertimos a entero
                opcion = int(input("Seleccione una opción: "))
                # Verificamos que la opción esté en el rango permitido
                if opcion in [1, 2, 3, 4, 5]:
                    break  # Si es válida, salimos del bucle
                else:
                    print("Opción no válida. Intente nuevamente.")
            except ValueError:
                # Capturamos el error si la entrada no es un número válido
                print("Por favor, ingrese un número válido.")

        if opcion == 1:
            # Opción para ingresar dinero
            while True:
                try:
                    # Pedimos la cantidad a depositar
                    cantidad = float(input("Ingrese la cantidad a depositar: "))
                    # Verificamos que la cantidad no sea negativa
                    if cantidad < 0:
                        print("No se pueden ingresar cantidades negativas. Intente nuevamente.")
                    else:
                        # Incrementamos el saldo y el contador de ingresos
                        saldo += cantidad
                        ingresos += 1
                        print(f"Se han ingresado {cantidad}. Nuevo saldo: {saldo:.2f}")
                        break  # Salimos del bucle
                except ValueError:
                    # Capturamos el error si la entrada no es un número válido
                    print("Por favor, ingrese un número válido.")

        elif opcion == 2:
            # Opción para retirar dinero
            while True:
                try:
                    # Pedimos la cantidad a retirar
                    cantidad = float(input("Ingrese la cantidad a retirar: "))
                    # Verificamos que la cantidad no sea negativa
                    if cantidad < 0:
                        print("No se pueden retirar cantidades negativas. Intente nuevamente.")
                    elif cantidad > saldo:
                        # Verificamos que no se retire más de lo que hay en la cuenta
                        print("No se puede retirar más de lo que hay en la cuenta.")
                    else:
                        # Decrementamos el saldo y el contador de retiradas
                        saldo -= cantidad
                        retiradas += 1
                        print(f"Se han retirado {cantidad}. Nuevo saldo: {saldo:.2f}")
                        break  # Salimos del bucle
                except ValueError:
                    # Capturamos el error si la entrada no es un número válido
                    print("Por favor, ingrese un número válido.")

        elif opcion == 3:
            # Opción para mostrar el saldo actual
            print(f"Saldo actual: {saldo:.2f}")

        elif opcion == 4:
            # Opción para mostrar estadísticas de ingresos y retiradas
            print(f"Ingresos realizados: {ingresos}")
            print(f"Retiradas realizadas: {retiradas}")

        elif opcion == 5:
            # Opción para salir del programa
            print("Saliendo del programa...")
            break  # Salimos del bucle principal

# Verificamos que el script se está ejecutando directamente
if __name__ == "__main__":
    main()