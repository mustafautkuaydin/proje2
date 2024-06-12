from Personel import *

class Hemsire(Personel):
    def __init__(self,personel_no,ad,soyad,departman,maas,calisma_saati,sertifika,hastane):
        Personel.__init__(self,personel_no,ad,soyad,departman,maas)
        self.__calisma_saati = calisma_saati
        self.__sertifika = sertifika
        self.__hastane = hastane

    def set_calisma_saati(self, calisma_saati):
        self.__calisma_saati = calisma_saati

    def set_sertifika(self, sertifika):
        self.__sertifika = sertifika

    def set_hastane(self, hastane):
        self.__hastane = hastane

    def get_calisma_saati(self):
        return self.__calisma_saati
    
    def get_sertifika(self):
        return self.__sertifika
    
    def get_hastane(self):
        return self.__hastane
    
    def maas_arttir(self):
        artan_maas = self.__maas + 50*(self.__calisma_saati-8)
        self.set_maas(artan_maas)
    
    def __str__(self):
        return f"Personel no: {self.__personel_no}, Ad: {self.__ad}, Soyad: {self.__soyad}, Departman: {self.__departman}, Maas: {self.__maas}, Calisma saati: {self.__calisma_saati}, Sertifika: {self.__sertifika}, Hastane: {self.__hastane}"
