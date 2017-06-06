#!/usr/bin/env python
#-*-coding: utf-8 -*-

'''
Titulo: tfidf.py
Author: Giovani Nícolas Bettoni

'''


import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import re



cachedStopWords = stopwords.words("english")

def preProcess(texto):
    texto = texto.lower()
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(texto)
    filtered_words = filter(lambda token: token not in stopwords.words('english'), tokens)
    return " ".join(filtered_words)

def showPreProcess(i):
    sequence = []
    print("\n ----------------------------- TEXT {} ------------------------------".format(i+1))
    arquivo = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text{}.txt".format(i+1), "r")
    text = arquivo.read()
    print '[original] text: \n' + text
    print '[preProcess] words: \n' + preProcess(text)
    sequence[i+1] = preProcess(text)
    arquivo.close()
    return (i+1)

if __name__ == "__main__":
    # inicianting pre-processing of these 20 texts

    print ("Starting pre-processing...")

    processed = []
    for i in range(20):
        showPreProcess(i)
        

    print "\n End of pre-processing!"




