from hash_function import HashFunction
from file_manager import FileManager

class Menu:
    def __init__(self):
        self.__hash_function = HashFunction()
        self.__file_manager = FileManager()

    def inicializar_sistema(self):
        self.__file_manager.inicializar_main_file()

    def mostrar_menu(self):
        while True:
            print("\n" + "-"*50)
            print("SISTEMA DE ALMACENAMIENTO CON FUNCIÓN HASH")
            print("-"*50)
            print("1. Cargar datos")
            print("2. Buscar datos")
            print("3. Salir")
            print("-"*50)

            try:
                opcion = int(input("Seleccione una opción: "))

                if opcion == 1:
                    self.__cargar_datos()
                elif opcion == 2:
                    self.__buscar_datos()
                elif opcion == 3:
                    print("Gracias por usar el sistema.")
                    break
                else:
                    print("Opción inválida. Intente de nuevo.")
            except ValueError:
                print("Por favor, ingrese un número válido.")
    def __cargar_datos(self):
        print("\nCargando datos")

        punts = self.__file_manager.cargar_archivos_data()

        if not punts:
            print("No se encontraron datos para cargar")
            return
        
        print(f"Se encontraron {len(punts)} jugadas")

        registros_principales = 0
        colisiones = 0

        for play in punts:
            posicion = self.__hash_function.calcular_hash(
                play.get_Date(),
                play.get_qtr(),
                play.get_HomeTeam()
            )

            guardado_principal = self.__file_manager.guardar_registro(posicion, play)
            
            if guardado_principal:
                registros_principales 
            else:
                colisiones += 1
                self.__hash_function.registrar_colision()

        print(f"\nEstadísticas de carga:")
        print(f"Total de jugadas procesadas: {len(punts)}")
        print(f"Registros guardados en archivo principal: {registros_principales}")
        print(f"Colisiones detectadas: {colisiones}")
    
    def __buscar_datos(self):
        """Busca datos según la posición (llave hash) indicada por el usuario."""
        try:
            posicion = int(input("\nIngrese la posición a buscar (0-749): "))
            
            if posicion < 0 or posicion >= 750:
                print("Posición inválida. Debe estar entre 0 y 749.")
                return
            
            resultados = self.__file_manager.buscar_por_posicion(posicion)

            if not resultados:
                print(f"No se encontraron registros en la posición {posicion}.")
            else:
                print(f"\nSe encontraron {len(resultados)} registros en la posición {posicion}:")
                
                for i, play in enumerate(resultados):
                    origen = "Archivo Principal" if i == 0 else f"Archivo de Colisiones (Posición {i})"
                    print(f"\n[{origen}]")
                    print(play)
        except ValueError:
            print("Por favor, ingrese un número válido.")