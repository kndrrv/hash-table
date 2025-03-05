class PuntPlay: # se crea la clase para representar la jugada punt
    def __init__(self, GameID, AwayTeam, HomeTeam, Yards_Gained, qtr, time, Date):
        self.__GameID = GameID # ID del juego
        self.__AwayTeam = AwayTeam # equipo visita
        self.__HomeTeam = HomeTeam # equipo casa
        self.__YardsGained = Yards_Gained # distancia
        self.__qtr = qtr # cuarto
        self.__time = time # tiempo
        self.__Date = Date # fecha

# getters
    def get_GameID(self):
        return self.__GameID
    
    def get_AwayTeam(self):
        return self.__AwayTeam
    
    def get_HomeTeam(self):
        return self.__HomeTeam
    
    def get_YardsGained(self):
        return self.__YardsGained
    
    def get_qtr(self):
        return self.__qtr
    
    def get_time(self): # método para obtener el tiempo restante en el cuarto, en segundos
        try:
            minutes, seconds = self.__time.split(':') # divide el tiempo en minutos y segundos
            return int(minutes) * 60 + int(seconds)
        except ValueError: # manejo de errores
            print(f"Error en formato de tiempo: {self.__time}")
            return 0 # retorna 0 en caso de error
    
    def get_Date(self):
        return self.__Date
    
    def __str__(self): # método para representar la instancia como una cadena de texto
        return (f"Fecha: {self.__Date}, Tiempo: {self.__time}, Equipo visita: {self.__AwayTeam}, Equipo casa: {self.__HomeTeam}, Cuarto: {self.__qtr}, Distancia: {self.__YardsGained}")