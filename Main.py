from Personel import *
from Doktor import *
from Hemsire import *
from Hasta import *

Personel1 = Personel(1,"Ali","Yilmaz","Temizlik Gorevlisi",32000)
Personel2 = Personel(2,"Ayse","Gun","Sekreter",32000)
print(f"{Personel1}\n{Personel2}\n")

Doktor1 = Doktor(3,"Akif","Kol","Cocuk Doktoru",80000,"Cocuk Sagligi",3,"Tire Devlet Hastanesi")
Doktor2 = Doktor(4,"Fikret","Hanci","Dahiliye",80000,"Dahiliye",7,"Tire Devlet Hastanesi")
Doktor3 = Doktor(5,"Fatma","Soylu","Goz Hastaliklari",80000,"Goz Hastaliklari",12,"Tire Devlet Hastanesi")
print(f"{Doktor1}\n{Doktor2}\n{Doktor3}\n")

Hemsire1 = Hemsire(6,"Sila","Korkmaz","Dahiliye",30000,12,"Dahiliye","Tire Devlet Hastanesi")
Hemsire2 = Hemsire(7,"Hulya","Demir","Cocuk Sagligi",30000,15,"Cocuk Sagligi","Tire Devlet Hastanesi")
Hemsire3 = Hemsire(8,"Mehmet","Kul","Goz Hastaliklari",30000,20,"Goz Hastaliklari","Tire Devlet Hastanesi")
print(f"{Hemsire1}\n{Hemsire2}\n{Hemsire3}\n")

Hasta1 = Hasta(1,"Yagmur","Dere","11.12.2000","covid-19","SINOVAC asisi")
Hasta2 = Hasta(2,"Hakan","Aktan","08.10.1995","grip","Ilac")
Hasta3 = Hasta(1,"Sezen","Sanci","02.08.1988","farenjit","Ilac")
print(f"{Hasta1}\n{Hasta2}\n{Hasta3}\n")