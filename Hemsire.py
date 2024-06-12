# Personel.py yi import etme
from Personel import *

# Hemsire sinifini, Personel sinifindan kalitim yoluyla olusturma
class Hemsire(Personel):
    # Initializer metodu olsuturma ve private degiskenleri ekleme
    def __init__(self,personel_no,ad,soyad,departman,maas,calisma_saati,sertifika,hastane):
        # Ust sinif degiskenleri private oldugundan erismek icin super() kullanma
        super().__init__(personel_no,ad,soyad,departman,maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    # Private degiskene deger atamak icin set metotları
    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    def set_hastane(self, hastane):
        self.__hastane = hastane

    # Private degiskeni dondurmek icin get metotlari
    def get_calisma_saati(self):
        return self.__calisma_saati
    
    def get_sertifika(self):
        return self.__sertifika
    
    def get_hastane(self):
        return self.__hastane
    
    # Hemsirenin calisma saatine bakarak maas arttirmak icin maas_arttir metotu
    def maas_arttir(self):
        self.set_maas(self.get_maas()+500*(self.__calisma_saati-8))
    

    # Sinifi stringe cevirip dondurmek icin __str__
    def __str__(self):
        # Ust sinifdaki degiskenlere erismek icin super() kullanma
        return f"{super().__str__()}, Calisma saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"
