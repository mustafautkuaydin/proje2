from Personel import *

class Doktor(Personel):
    def __init__(self,personel_no,ad,soyad,departman,maas,uzmanlik,deneyim_yili,hastane):
        super().__init__(personel_no,ad,soyad,departman,maas)
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
    
    def maas_arttir(self):
        if self.__deneyim_yili >= 2 and self.__deneyim_yili <= 4:
            self.set_maas(self.get_maas() + 20000)
        if self.__deneyim_yili >= 5 and self.__deneyim_yili <= 9:
            self.set_maas(self.get_maas() + 30000)
        if self.__deneyim_yili > 10:
            self.set_maas(self.get_maas() + 35000)

    def __str__(self):
        return f"{super().__str__()}, Uzmanlik: {self.__uzmanlik}, Deneyim yili: {self.__deneyim_yili}, Hastane: {self.__hastane}"
