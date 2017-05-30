#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'User'

import os
d=os.path.dirname(__file__)

import turkceYazim
from difflib import SequenceMatcher

#d = os.getcwd()
d = d=os.path.dirname(__file__)
os.environ["CLASSPATH"] = os.path.join(os.path.join(d,"jar"),"zemberek-tum-2.0.jar")
os.environ.update()

from jnius import autoclass

#java kutuphaneleri
zemberek_class=autoclass('net.zemberek.erisim.Zemberek') #Javadan zemberek sinifi cagriliyor
turkiye_turkcesi=autoclass('net.zemberek.tr.yapi.TurkiyeTurkcesi') #Turkce dili yukleniyor

ZEMBEREK=zemberek_class(turkiye_turkcesi())

#search by letter
def WordSearch(char,wordList):
    wordFoundList=[]
    for wl in wordList:
        for ch in char:
            if wl.startswith(ch):
                wordFoundList.append(wl)
    return wordFoundList

def closeMatch(word, match_word):

    first = match_word[0:2] # first two letters
    back = match_word[-1] # end letter

    #keeping with the rule that first two and last letters must be the same as the word
    for i in range(len(word)):
        # checks if the word starts with (startswith function) the front letter
        if word == match_word:
            return 1.0
        elif word.startswith(first) and word[-1].endswith(back):
           ratioScore=SequenceMatcher(None, word, match_word).ratio()
           #with the use of the difflib library I now have value to logic test also
           return ratioScore
    else:
        return 0

def spellingLetter(wordCorrect):
    #sorunlu harfler
    turkce_kok=turkceYazim.turkce_kok#sorunlu turkce harfler
    english_kok=turkceYazim.english_kok#sorunlu english harfler

    #sozluk yukleniyor
    word_list=open("veriler/kelime-listesi.txt","r").read().decode("utf-8").split("\n")
    open("veriler/kelime-listesi.txt","r").close()

    word=wordCorrect

    char=[]
    # aranacak kelime listesini bas harfine gore kisaltiyorum
    try:
        if word[0] in english_kok:
            char.append(word[0])
            char.append(turkce_kok[english_kok.index(word[0])])
        else: char.append(word[0])
    except:
        pass
 
#    Aranacak kelime listesi
    wordList=WordSearch(char,word_list)
#    print wordList
    
    maxCostMach=0.7
    resultMach={}
    for dicText in wordList:
        #cost_mach=SequenceMatcher(None,wordNew,dicText).ratio()#maliyet
        cost_mach=closeMatch(word,dicText)
        if cost_mach>=maxCostMach:
            #maxCostMach=cost_mach
            resultMach[dicText]=cost_mach
#    print resultMach
    return [key for key,val in resultMach.iteritems() if val == max(resultMach.values())]

if __name__ == '__main__':
#    listele=["suprizler".decode("utf-8"),"şuprizler".decode("utf-8"),"süprizler".decode("utf-8"),
#             "suprızler".decode("utf-8"),"şüprizler".decode("utf-8"),"şuprızler".decode("utf-8"),
#             "süprızler".decode("utf-8"),"şüprızler".decode("utf-8")]
    
    listele=["yasamislar".decode("utf-8"),"yaşamislar".decode("utf-8"),
             "yasamıslar".decode("utf-8"), "yasamişlar".decode("utf-8"),
             "yaşamıslar".decode("utf-8"), "yaşamişlar".decode("utf-8"),
             "yasamışlar".decode("utf-8"), "yaşamışlar".decode("utf-8")]
    
    for l in listele:
        print spellingLetter(l)