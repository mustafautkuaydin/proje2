class Personel():
    def __init__(self,hasta_no,ad,soyad,dogum_tarihi,hastalik,tedavi):
        self.__hasta_no = hasta_no
        self.__ad = ad
        self.__soyad = soyad
        self.__dogum_tarihi = dogum_tarihi
        self.__hastalik = hastalik
        self.__tedavi = tedavi

    def set_hasta_no(self, hasta_no):
        self.__hasta_no = hasta_no

    def set_ad(self, ad):
        self.__ad = ad
        
    def set_soyad(self, soyad):
        self.__soyad = soyad

    def set_dogum_tarihi(self, dogum_tarihi):
        self.__dogum_tarihi = dogum_tarihi

    def set_tedavi(self, tedavi):
        self.__tedavi = tedavi
    
    def set_hasta_no(self, hasta_no):
        self.__hasta_no = hasta_no

    def get_hasta_no(self):
        return self.__hasta_no
    
    def get_ad(self):
        return self.__ad
    
    def get_soyad(self):
        return self.__soyad
    
    def get_dogum_tarihi(self):
        return self.__dogum_tarihi
    
    def get_hastalik(self):
        return self.__hastalik
    
    def get_tedavi(self):
        return self.__tedavi
    
    def __str__(self):
        return f"{self.__hasta_no}{self.__ad}{self.__soyad}{self.__dogum_tarihi}{self.__hastalik}{self.__tedavi}"
