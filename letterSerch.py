#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'User'

import os

print os.path.dirname(__file__)

import turkceYazim, math, spellingLetter
import levenshteinLib as levlib


d=os.path.dirname(__file__)
#d = os.getcwd()
os.environ["CLASSPATH"] = os.path.join(os.path.join(d,"jar"),"zemberek-tum-2.0.jar")
os.environ.update()

from jnius import autoclass

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

#java kutuphaneleri
zemberek_class=autoclass('net.zemberek.erisim.Zemberek') #Javadan zemberek sinifi cagriliyor
turkiye_turkcesi=autoclass('net.zemberek.tr.yapi.TurkiyeTurkcesi') #Turkce dili yukleniyor

ZEMBEREK=zemberek_class(turkiye_turkcesi())

def CheckList(ch,wList,turkce_kok,english_kok):

    english_kok=english_kok
    turkce_kok=turkce_kok
    n=len(ch)#düzeltilecek kelime sayısı

    i=0 #dizi index'i
    while i<int(math.pow(2,n)-n):
        for j in range(0,n):
            wordTemp=list(wList[i])
            if wordTemp[ch[j]] in english_kok:
                wordTemp[ch[j]]=turkce_kok[english_kok.index(wordTemp[ch[j]])]
                wordTemp="".join(wordTemp)
                if wordTemp != "" and wordTemp not in wList:
                    wList.append(wordTemp)
        i+=1

def letterSearch(worngW):
    #sorunlu harfler
    turkce_kok=turkceYazim.turkce_kok
    english_kok=turkceYazim.english_kok
    vowel=turkceYazim.vowel
    consonant=turkceYazim.consonant
    wtempList=[]

    wList=list(worngW)
    #check again letter
    word="";count_=1;i=0;
    while i<len(wList)-1:
        if wList[i]==wList[i+1]:
            for j in range(i, (len(wList)-1)):
                if wList[j]==wList[j+1]:
                    count_+=1
                else:
                    break
        word +=word.join(wList[i])

        if (wList[i] in vowel and wList[i+1] in vowel) or (wList[i] in consonant and wList[i+1] in consonant):#iki sesli harf yan yana yazılmaz
             i+=count_
        else : i+=1

        count_=1
        if i==(len(wList)-1):#en son elemani ekle
           word +=word.join(wList[i])

    #to derive the word
    n=len(word)#word lengh
    ch=[];#adım sayımızı tutuyor
    #duzeltilecek harf indexleri
    for i in range(0,n):
        if word[i] in english_kok:
            ch.append(i)

    wtempList.append(word)
    CheckList(ch,wtempList,turkce_kok,english_kok)
    
    
    #check word for turkish
    wordNewList=[]
    for i in range (0, len(wtempList)):
        sonuc=ZEMBEREK.kelimeCozumle(wtempList[i])#checke word for turkish
        if sonuc !=[]:#splite root
            if wtempList[i] not in wordNewList:
                wordNewList.append(wtempList[i])
        else:
            temps=spellingLetter.spellingLetter(wtempList[i])
            for temp in temps:
                sonuc=ZEMBEREK.kelimeCozumle(temp)#checke word for turkish
                if sonuc !=[]:#splite root
                    if temp not in wordNewList:
                        wordNewList.append(temp)

    #en benzer kelimeyi geri dönderiyoruz
    wNewList={}
    maxCostLev=0.6
    
#    print wordNewList
    
    for text in wordNewList:
        cost_lev=float(levlib.levenshtein_7(word,text))/len(list(text))#maliyet, 0'a ne kadar yakin ise o kadar benzer demektir
        if cost_lev<=maxCostLev:
            wNewList[text]=cost_lev
#    print wNewList
    #print wordNewList
    wordSim=[key for key,val in wNewList.iteritems() if val == min(wNewList.values())]
    
#    if wordSim!=[]:
#        result=ZEMBEREK.kelimeCozumle(wordSim[0])
#        if result !=[]:
#            return [str(result[0].kok().icerik()).decode("utf-8"),wordSim[0]]
    return wordSim

if __name__ == '__main__':
    w=letterSearch("yasatmislar".decode("utf-8"))
    print w
