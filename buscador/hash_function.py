class HashFunction: # clase para implementar la función hash para el sistema de almacenamiento
    
    def __init__(self, tamaño_tabla = 750): # inicializa la función hash con el tamaño de tabla solicitado 750
        self.__tamaño_tabla = tamaño_tabla
        self.__colisiones = 0

    def calcular_hash(self, fecha, cuarto, equipo_visita): # procesa la fecha
        fecha_sin_barras = fecha.replace('/', '')
        suma_fecha = sum(int(digito) for digito in fecha_sin_barras if digito.isdigit())
        
        valor_cuarto = int(cuarto) # valor del cuarto

        primeras_letras = equipo_visita[:3].upper() # procesa el equipo local, las primeras 3 letras o menos si es más corto
        suma_letras = sum(ord(letra) for letra in primeras_letras)

        hash_value = (suma_fecha + valor_cuarto + suma_letras) % self.__tamaño_tabla # combina y lo aplica al módulo

        return hash_value

    def registrar_colision(self):
        self.__colisiones += 1 # incrementa el contador de colisiones

    def obtener_estadisticas(self): # devuelve estadísticas sobre el uso del hash
        return {
            'colisiones': self.__colisiones,
            'tamaño_tabla': self.__tamaño_tabla
        }