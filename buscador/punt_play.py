class PuntPlay:
    def __init__(self, GameID, AwayTeam, HomeTeam, Yards_Gained, qtr, time, Date):
        self.__GameID = GameID
        self.__AwayTeam = AwayTeam
        self.__HomeTeam = HomeTeam
        self.__YardsGained = Yards_Gained
        self.__qtr = qtr
        self.__time = time
        self.__Date = Date

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
    
    def get_time(self):
        try:
            minutes, seconds = self.__time.split(':')
            return int(minutes) * 60 + int(seconds)
        except ValueError:
            print(f"Error en formato de tiempo: {self.__time}")
            return 0
    
    def get_Date(self):
        return self.__Date
    
    def __str__(self):
        return (f"Fecha: {self.__Date}, Tiempo: {self.__time},
                Equipo visita: {self.__AwayTeam}, Equipo casa: {self.__HomeTeam},
                Cuarto: {self.__qtr}, Distancia: {self.__YardsGained}")