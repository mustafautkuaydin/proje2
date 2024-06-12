# Personel.py yi import etme
from Personel import *

# Doktor sinifini, Personel sinifindan kalitim yoluyla olusturma
class Doktor(Personel):
    # Initializer metodu olsuturma ve private degiskenleri ekleme
    def __init__(self,personel_no,ad,soyad,departman,maas,uzmanlik,deneyim_yili,hastane):
        # Ust sinif degiskenleri private oldugundan erismek icin super() kullanma
        super().__init__(personel_no,ad,soyad,departman,maas)
        self.__uzmanlik = uzmanlik
        self.__deneyim_yili = deneyim_yili
        self.__hastane = hastane

    # Private degiskene deger atamak icin set metotları
    def set_uzmanlik(self, uzmanlik):
        self.__uzmanlik = uzmanlik

    def set_deneyim_yili(self, deneyim_yili):
        self.__deneyim_yili = deneyim_yili

    def set_hastane(self, hastane):
        self.__hastane = hastane

    # Private degiskeni dondurmek icin get metotlari
    def get_uzmanlik(self):
        return self.__uzmanlik
    
    def get_deneyim_yili(self):
        return self.__deneyim_yili
    
    def get_hastane(self):
        return self.__hastane
    
    # Doktorun deneyim yilina bakarak maas arttirmak icin maas_arttir metotu
    def maas_arttir(self):
        if self.__deneyim_yili >= 2 and self.__deneyim_yili <= 4:
            self.set_maas(self.get_maas() + 20000)
        if self.__deneyim_yili >= 5 and self.__deneyim_yili <= 9:
            self.set_maas(self.get_maas() + 30000)
        if self.__deneyim_yili > 10:
            self.set_maas(self.get_maas() + 35000)

    # Sinifi stringe cevirip dondurmek icin __str__
    def __str__(self):
        # Ust sinifdaki degiskenlere erismek icin super() kullanma
        return f"{super().__str__()}, Uzmanlik: {self.__uzmanlik}, Deneyim yili: {self.__deneyim_yili}, Hastane: {self.__hastane}"
