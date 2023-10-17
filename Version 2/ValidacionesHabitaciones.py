class ValidacionesHabitaciones:

  def validacionPiso(self):
      bucle1=0

      while bucle1 !=1:
            print(f"*** Ingresar piso ***")
            print("Piso 0")
            print("Piso 1")
            print("Piso 2")
            print("Piso 3")
            print("Piso 4")

            eleccion = input("Ingrese el número de la opción: ")

            if eleccion == "1":
                piso = 1
                return piso
            elif eleccion == "2":             
                piso = 2
                return piso
              
            elif eleccion == "2":             
                piso = 3
                return piso
            elif eleccion == "2":             
                piso = 4
                return piso
            else:
                print("Error Opción no válida ---> Por favor seleccione una opción válida")