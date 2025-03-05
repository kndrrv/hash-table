from punt_play import PuntPlay
import os
import struct as struct
import pickle as pickel

class FileManager: # clase para manejar la lectura y escritura de archivos del sistema de almacenamientos}
    def __init__(self, data_path = "C:/data/segundaprogramada"):
        self.__data_path = data_path
        self.__main_file = os.path.join(data_path, "info.dat")
        self.__record_size = 1024

    def inicializar_main_file(self, size = 750):
        if not os.path.exists(self.__main_file):
            os.makedirs(os.path.dirname(self.__main_file), exist_ok = True)

            with open(self.__main_file, 'wb') as f:
                for _ in range(size):
                    empty_record = bytearray(self.__record_size)
                    f.write(empty_record)
                print(f"Archivo {self.__main_file} creado con {size} registros vacíos")

        else:
            print(f"El archivo {self.__main_file} ya existe")

    def guardar_registro(self, position, punt_play):

        vacío = self.revisar_si_posicion_vacia(position)

        serializar_data = pickel.dumps(punt_play)

        if len(serializar_data) > self.__record_size:
            print(f"Error: el objeto es demasiado grande ({len(serializar_data)} bytes) para el tamaño de registro ({self.__record_size} bytes)")

        serializar_data = serializar_data.ljust(self.__record_size, b'\x00')

        if vacío:
            with open(self.__main_file, 'r+b') as f:
                f.seek(position * self.__record_size)
                f.write(serializar_data)
            return True
        else:
            archivo_colision = os.path.join(os.path.dirname(self.__main_file), f"{position}-col.dat")

            mode = 'ab' if os.path.exists(archivo_colision) else 'wb'

            with open(archivo_colision, mode) as f:
                f.write(serializar_data)

            return False
        
    def revisar_si_posicion_vacia(self, position):
        with open(self.__main_file, 'rb') as f:
            f.seek(position * self.__record_size)
            data = f.read(self.__record_size)
            return all(b == 0 for b in data)
        
    def cargar_archivos_data(self):
        punts = []
        print(f"Buscando archivos CSV en: {self.__data_path}")
        print(f"Contenido del directorio: {os.listdir(self.__data_path)}")

        for filename in os.listdir(self.__data_path):
            file_path = os.path.join(self.__data_path, filename)
            print(f"Procesando archivo: {file_path}")
            try:
                with open(file_path, 'r', encoding = 'utf-8') as file:
                    file.readline()

                    header = file.readline().strip().split(',')

                    for line in file:
                        fields = line.strip().split(',')
                        if len(fields) >=7:
                            date = fields[0]
                            time = fields[1]
                            AwayTeam = fields[2]
                            HomeTeam = fields[3]
                            try:
                                qtr = int(fields[4])
                            except ValueError:
                                print(f"Saltando linea debido a cuarto inválido: {line}")
                                continue

                            YardsGained = fields[5]
                            GameID = fields[6]

                            play = PuntPlay(GameID, AwayTeam, HomeTeam, YardsGained, qtr, time, date)
                            punts.append(play)
            except Exception as e:
                print(f"Error al cargar el archivo {filename}: {e}")
        return punts
    def buscar_por_posicion(self, position):
        resultados = []

        if position < 0 or position >= 750:
            print(f"Posición inválida: {position}. Debe estar entre 0 y 749")
            return resultados
        
        try:
            with open(self.__main_file, 'rb') as f:
                f.seek(position * self.__record_size)
                main_data = f.read(self.__record_size)

                if not all(b == 0 for b in main_data):
                    main_data = main_data.rstrip(b'\x00')
                    try:
                        punt_play = pickel.loads(main_data)
                        resultados.append(punt_play)
                    except Exception as e:
                        print(f"Error al deserealizar el registro: {e}")
        except Exception as e:
            print(f"Error al leer el archivo principal: {e}")

        archivo_colision = os.path.join(os.path.dirname(self.__main_file), f"{position}-col.dat")
        if os.path.exists(archivo_colision):
            try:
                with open(archivo_colision, 'rb') as f:
                    while True:
                        col_data = f.read(self.__record_size)
                        if not col_data:
                            break
                        col_data = col_data.rstrip(b'\x00')

                        try:
                            punt_play = pickel.loads(col_data)
                            resultados.append(punt_play)
                        except Exception as e:
                            print(f"Error al deserealizar un registro de colisión: {e}")
            except Exception as e:
                print(f"Error al leer el archivo de colisiones: {e}")

        return resultados
