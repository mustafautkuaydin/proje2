from Personel import *
from Doktor import *
from Hemsire import *
from Hasta import *

Personel1 = Personel(1,"Ali","Yilmaz","Temizlik Gorevlisi",32000)
Personel2 = Personel(2,"Ayse","Gun","Sekreter",32000)
print(f"{Personel1}\n{Personel2}")

Doktor1 = Doktor(3,"Akif","Kol","Cocuk Doktoru",80000,"Cocuk Sagligi",3,"Tire Devlet Hastanesi")

Doktor2 = Doktor(4,"Fikret","Hanci","Dahiliye",80000,"Dahiliye",7,"Tire Devlet Hastanesi")

Doktor3 = Doktor(5,"Fatma","Soylu","Goz Hastaliklari",80000,"Goz Hastaliklari",12,"Tire Devlet Hastanesi")

print(f"{Doktor1}\n{Doktor2}\n{Doktor3}")