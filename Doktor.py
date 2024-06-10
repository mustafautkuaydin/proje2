class Doktor():
    def __init__(self,uzmanlik,deneyim_yili,hastane):
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def get_uzmanlik(self):
        return self.__uzmanlik
    
    def get_deneyim_yili(self):
        return self.__deneyim_yili
    
    def get_hastane(self):
        return self.__hastane
    
    def __str__(self):
        return f"{self.__uzmanlik}{self.__deneyim_yili}{self.__hastane}"
