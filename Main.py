import pandas as pd
from Personel import *
from Doktor import *
from Hemsire import *
from Hasta import *

Personel1 = Personel(1,"Ali","Yilmaz","Temizlik Gorevlisi",5000)
Personel2 = Personel(2,"Ayse","Gun","Sekreter",6000)
print(f"{Personel1}\n{Personel2}\n")

Doktor1 = Doktor(3,"Akif","Kol","Cocuk Doktoru",80000,"Cocuk Sagligi",3,"Tire Devlet Hastanesi")
Doktor2 = Doktor(4,"Fikret","Hanci","Dahiliye",80000,"Dahiliye",7,"Tire Devlet Hastanesi")
Doktor3 = Doktor(5,"Fatma","Soylu","Dahiliye",80000,"Dahiliye",12,"Tire Devlet Hastanesi")
Doktor.maas_arttir(Doktor1)
Doktor.maas_arttir(Doktor2)
Doktor.maas_arttir(Doktor3)
print(f"{Doktor1}\n{Doktor2}\n{Doktor3}\n")

Hemsire1 = Hemsire(6,"Sila","Korkmaz","Dahiliye",30000,50,"Dahiliye","Tire Devlet Hastanesi")
Hemsire2 = Hemsire(7,"Hulya","Demir","Cocuk Sagligi",30000,55,"Cocuk Sagligi","Tire Devlet Hastanesi")
Hemsire3 = Hemsire(8,"Mehmet","Kul","Dahiliye",30000,45,"Dahiliye","Tire Devlet Hastanesi")
Hemsire.maas_arttir(Hemsire1)
Hemsire.maas_arttir(Hemsire2)
Hemsire.maas_arttir(Hemsire3)
print(f"{Hemsire1}\n{Hemsire2}\n{Hemsire3}\n")

Hasta1 = Hasta(1,"Yagmur","Dere",2000,"covid-19","SINOVAC asisi")
Hasta2 = Hasta(2,"Hakan","Aktan",1995,"grip","Ilac")
Hasta3 = Hasta(3,"Sezen","Sanci",1988,"farenjit","Ilac")
print(f"{Hasta1}\n{Hasta2}\n{Hasta3}\n")

pd.set_option('display.max_columns', None)

Ozellikler = [
    {"personel_no":1, "ad":"Ali", "soyad":"Yilmaz", "departman":"Temizlik Gorevlisi", "maas":5000, "uzmanlik":0, "deneyim_yili": 0, "hastane":0, "calisma_saati":0, "sertifika":0, "hasta_no":0, "dogum_tarihi":0, "hastalik":0, "tedavi":0},
    {"personel_no":2, "ad":"Ayse", "soyad":"Gun", "departman":"Sekreter", "maas":6000, "uzmanlik":0, "deneyim_yili": 0, "hastane":0, "calisma_saati":0, "sertifika":0, "hasta_no":0, "dogum_tarihi":0, "hastalik":0, "tedavi":0},
    {"personel_no":3, "ad":"Akif", "soyad":"Kol", "departman":"Cocuk Doktoru", "maas":100000, "uzmanlik":"Cocuk Sagligi", "deneyim_yili": 3, "hastane":"Tire Devlet Hastanesi", "calisma_saati":0, "sertifika":0, "hasta_no":0, "dogum_tarihi":0, "hastalik":0, "tedavi":0},
    {"personel_no":4, "ad":"Fikret", "soyad":"Hanci", "departman":"Dahiliye", "maas":110000, "uzmanlik":"Dahiliye", "deneyim_yili": 7, "hastane":"Tire Devlet Hastanesi", "calisma_saati":0, "sertifika":0, "hasta_no":0, "dogum_tarihi":0, "hastalik":0, "tedavi":0},
    {"personel_no":5, "ad":"Fatma", "soyad":"Soylu", "departman":"Dahiliye", "maas":115000, "uzmanlik":"Dahiliye", "deneyim_yili": 12, "hastane":"Tire Devlet Hastanesi", "calisma_saati":0, "sertifika":0, "hasta_no":0, "dogum_tarihi":0, "hastalik":0, "tedavi":0},
    {"personel_no":6, "ad":"Sila", "soyad":"Korkmaz", "departman":"Dahiliye", "maas":51000, "uzmanlik":0, "deneyim_yili": 0, "hastane":"Tire Devlet Hastanesi", "calisma_saati":50, "sertifika":"Dahiliye", "hasta_no":0, "dogum_tarihi":0, "hastalik":0, "tedavi":0},
    {"personel_no":7, "ad":"Hulya", "soyad":"Demir", "departman":"Cocuk Sagligi", "maas":53500, "uzmanlik":0, "deneyim_yili": 0, "hastane":"Tire Devlet Hastanesi", "calisma_saati":55, "sertifika":"Cocuk Sagligi", "hasta_no":0, "dogum_tarihi":0, "hastalik":0, "tedavi":0},
    {"personel_no":8, "ad":"Mehmet", "soyad":"Kul", "departman":"Dahiliye", "maas":48500, "uzmanlik":0, "deneyim_yili": 0, "hastane":"Tire Devlet Hastanesi", "calisma_saati":45, "sertifika":"Dahiliye", "hasta_no":0, "dogum_tarihi":0, "hastalik":0, "tedavi":0},
    {"personel_no":0, "ad":"Yagmur", "soyad":"Dere", "departman":0, "maas":0, "uzmanlik":0, "deneyim_yili": 0, "hastane":0, "calisma_saati":0, "sertifika":0, "hasta_no":1, "dogum_tarihi":2000, "hastalik":"covid-19", "tedavi":"SINOVAC asisi"},
    {"personel_no":0, "ad":"Hakan", "soyad":"Aktan", "departman":0, "maas":0, "uzmanlik":0, "deneyim_yili": 0, "hastane":0, "calisma_saati":0, "sertifika":0, "hasta_no":2, "dogum_tarihi":1995, "hastalik":"grip", "tedavi":"Ilac"},
    {"personel_no":0, "ad":"Sezen", "soyad":"Sanci", "departman":0, "maas":0, "uzmanlik":0, "deneyim_yili": 0, "hastane":0, "calisma_saati":0, "sertifika":0, "hasta_no":3, "dogum_tarihi":1988, "hastalik":"farenjit", "tedavi":"Ilac"},
    ]

df = pd.DataFrame(Ozellikler)

# Doktorları uzmanlıga gore gruplama
uzman_doktor_grubu = df[df["uzmanlik"] != 0].groupby("uzmanlik")
print(f"Uzmanlik alanina göre doktor sayisi:\n\n{uzman_doktor_grubu.count()}\n\n")

deneyimli_doktor = df[df["deneyim_yili"] > 5]
print(f"Deneyim yili 5 yildan fazla olan doktorlar:\n\n{deneyimli_doktor}\n\n")

hasta_siralama = df[df["hastalik"]!=0 ].sort_values("ad")
print(f"Hasta adlarini alfabetik siralama:\n\n{hasta_siralama}\n\n")

para_siralama = df[df["maas"]>7000]
print(f"Maasi 7000 den fazla olan personeller:\n\n{para_siralama}\n\n")

hasta_yas_siralama = df[df["dogum_tarihi"]>=1990]
print(f"Dogum yili 1990 ve sonrasi olan hastalar:\n\n{hasta_yas_siralama}\n\n")

yeniDataFrame=df[["ad","soyad","departman","maas","uzmanlik","deneyim_yili","hastalik","tedavi"]]
print(f"Yeni DataFrame:\n\n{yeniDataFrame}\n\n")