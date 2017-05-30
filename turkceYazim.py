#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'User'


#sorunlu harfler
turkce_kok=["ç".decode("utf-8"),"ş".decode("utf-8"),"ı".decode("utf-8"),
            "ü".decode("utf-8"),"ğ".decode("utf-8"),"ö".decode("utf-8")]
english_kok=["c".decode("utf-8"),"s".decode("utf-8"),"i".decode("utf-8"),
            "u".decode("utf-8"),"g".decode("utf-8"),"o".decode("utf-8")]

consonant= "bcçdfgğhjklmnprsştvyz".decode("utf-8")#sesiz harfler
vowel= "aeıioöuü".decode("utf-8")#sesli harfler

#turkce baglaclar listesi
tumBaglaclar=["ama".decode("utf-8"),"amma".decode("utf-8"),"velakin".decode("utf-8"),"ancak".decode("utf-8"),
              "belki".decode("utf-8"),"bile".decode("utf-8"),"bre".decode("utf-8"),"çünkü".decode("utf-8"),
              "da".decode("utf-8"),"de".decode("utf-8"),"dahi".decode("utf-8"),"eğer".decode("utf-8"),
              "fakat".decode("utf-8"),"gelgelelim".decode("utf-8"),"gerek".decode("utf-8"),"ha".decode("utf-8"),
              "hâlbuki".decode("utf-8"),"hatta".decode("utf-8"),"hele".decode("utf-8"),"hem".decode("utf-8"),
              "ile".decode("utf-8"),"ille".decode("utf-8"),"ister".decode("utf-8"),"ki".decode("utf-8"),
              "kim".decode("utf-8"),"lakin".decode("utf-8"),"madem".decode("utf-8"),"mademki".decode("utf-8"),
              "meğer".decode("utf-8"),"meğerki".decode("utf-8"),"meğerse".decode("utf-8"),"ne".decode("utf-8"),
              "neyse".decode("utf-8"),"oysa".decode("utf-8"),"oysaki".decode("utf-8"),"şayet".decode("utf-8"),
              "ve".decode("utf-8"),"velev".decode("utf-8"),"veya".decode("utf-8"),"veyahut".decode("utf-8"),
              "ya".decode("utf-8"),"ya da".decode("utf-8"),"yahut".decode("utf-8"),"yalnız".decode("utf-8"),
              "yani".decode("utf-8"),"yok".decode("utf-8"),"yoksa".decode("utf-8"),"zira".decode("utf-8")]

#turkce edat listesi
tumEdatlar=["başka".decode("utf-8"),"beri".decode("utf-8"),"dâir".decode("utf-8"),"doğru".decode("utf-8"),
            "değin".decode("utf-8"),"denli".decode("utf-8"),"dek".decode("utf-8"),"dolayı".decode("utf-8"),
            "diye".decode("utf-8"),"evvel".decode("utf-8"),"gayri".decode("utf-8"),"gibi".decode("utf-8"),
            "göre".decode("utf-8"),"için".decode("utf-8"),"ile".decode("utf-8"),
            "karşı".decode("utf-8"),"karşın".decode("utf-8"),"önce".decode("utf-8"),"ötürü".decode("utf-8"),
            "öte".decode("utf-8"),"rağmen".decode("utf-8"),"sanki".decode("utf-8"),"sonra".decode("utf-8"),
            "sıra".decode("utf-8"),"üzere".decode("utf-8"),"mi".decode("utf-8"),"değil".decode("utf-8"),
            "nâşi".decode("utf-8"),"nazaran".decode("utf-8")]

#turkce zarflar listesi
tumZarflar=["dün".decode("utf-8"), "bugün".decode("utf-8"), "yarın".decode("utf-8"), "akşam".decode("utf-8"),
            "sabah".decode("utf-8"),"öğle".decode("utf-8"),"ikindi".decode("utf-8"),"gece".decode("utf-8"),
            "kışın".decode("utf-8"),"sabahleyin".decode("utf-8"),"öğleleyin".decode("utf-8"),"akşamleyin".decode("utf-8"),
            "geceleyin".decode("utf-8"), "ilkin".decode("utf-8"), "şimdilik".decode("utf-8"), "yine".decode("utf-8"),
            "demin".decode("utf-8"),"şimdi".decode("utf-8"), "daha".decode("utf-8"),"hâlâ".decode("utf-8"),
            "henüz".decode("utf-8"), "derhal".decode("utf-8"), "bazen".decode("utf-8"),"ileri".decode("utf-8"),
            "geri".decode("utf-8"), "aşağı".decode("utf-8"),"yukarı".decode("utf-8"),"beri".decode("utf-8"),
            "yan".decode("utf-8"),"neden".decode("utf-8"),"niye".decode("utf-8"),"niçin".decode("utf-8"),
            "nasıl".decode("utf-8"), "zaman".decode("utf-8")]

cikan=["biraz".decode("utf-8"),"birçok".decode("utf-8"), "fazla".decode("utf-8"), "çok".decode("utf-8"),"kadar".decode("utf-8"),
       "en".decode("utf-8"), "pek".decode("utf-8"), "az".decode("utf-8"),"çoğu".decode("utf-8"),"birkaç".decode("utf-8")]
#turkce isaret sifatlari
tumSifatlari=["o".decode("utf-8"),"ben".decode("utf-8"),"sen".decode("utf-8"),"bu".decode("utf-8"),"şu".decode("utf-8"),
              "biz".decode("utf-8"),"siz".decode("utf-8"),"onlar".decode("utf-8"),"bunlar".decode("utf-8"),
              "şunlar".decode("utf-8"),"başka".decode("utf-8"),"bâzı".decode("utf-8"),"bir".decode("utf-8"),
              "biraz".decode("utf-8"),"birtakım".decode("utf-8"),"bütün".decode("utf-8"),"diğer".decode("utf-8"),
              "falanca".decode("utf-8"),"filanca".decode("utf-8"),"her".decode("utf-8"),"herhangi".decode("utf-8"),
              "hiç".decode("utf-8"),"hiçbir".decode("utf-8"),
              "kimi".decode("utf-8"),"nice".decode("utf-8"),"öbür".decode("utf-8"),"tüm".decode("utf-8"),
              "uzun".decode("utf-8"),"kısa".decode("utf-8"),"geniş".decode("utf-8"),"dar".decode("utf-8"),
              "yeşil".decode("utf-8"),"kırmızı".decode("utf-8"),"sarı".decode("utf-8"),"pembe".decode("utf-8"),
              "beyaz".decode("utf-8"),"siyah".decode("utf-8"),"mor".decode("utf-8"),"turuncu".decode("utf-8")]

turkceKisaltmalkar={"hngr":"hüngür".decode("utf-8"),"gzel":"güzel".decode("utf-8"),"kib":"kendine iyi bak".decode("utf-8"),
                    "grşrz":"görüşürüz".decode("utf-8"), "slm":"selam".decode("utf-8"), "mrb":"merhaba".decode("utf-8"),
                    "aeo":"allaha emanet ol".decode("utf-8"), "tmm":"tamam".decode("utf-8")}
#turkiyedeki sehir isimleri
sehirIsimleri=open("veriler/sehir-isimleri.txt","r").read().lower().decode("utf-8").split("\n")
open("veriler/il-isimleri.txt","r").close()

#turkiyedeki ilce isimleri
ilceIsimleri=open("veriler/ilce-isimleri.txt","r").read().lower().decode("utf-8").split("\n")
open("veriler/ilce-isimleri.txt","r").close()

#turkiyedeki ilce isimleri
ulkeIsimleri=open("veriler/ulke-isimleri.txt","r").read().lower().decode("utf-8").split("\n")
open("veriler/ulke-isimleri.txt","r").close()

#turkiyedeki kisi isimleri
kisiIsimleri=open("veriler/kisi-isimleri.txt","r").read().lower().decode("utf-8").split("\n")
open("veriler/kisi-isimleri.txt","r").close()
