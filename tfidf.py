#!/usr/bin/env python
#-*-coding: utf-8 -*-

'''
Titulo: tfidf.py
Author: Giovani Nícolas Bettoni

'''


import string
import re
import nltk
import string
import pprint
from nltk.corpus import stopwords
from nltk import word_tokenize
from math import log
from numpy import dot
from numpy.linalg import norm

doc_list = []

# inicianting pre-processing of these 20 texts

print (" -> Starting pre-processing...")

arquivo1 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text1.txt", "r")
text1 = arquivo1.read()
stop1 = stopwords.words('english') + list(string.punctuation)
tokens1 = [i for i in word_tokenize(text1.lower()) if i not in stop1]
print tokens1

arquivo2 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text2.txt", "r")
text2 = arquivo2.read()
stop2 = stopwords.words('english') + list(string.punctuation)
tokens2 = [i for i in word_tokenize(text2.lower()) if i not in stop2]

arquivo3 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text3.txt", "r")
text3 = arquivo3.read()
stop3 = stopwords.words('english') + list(string.punctuation)
tokens3 = [i for i in word_tokenize(text3.lower()) if i not in stop3]

#just for tests
# arquivo4 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text4.txt", "r")
# text4 = arquivo4.read()
# stop4 = stopwords.words('english') + list(string.punctuation)
# tokens4 = [i for i in word_tokenize(text4.lower()) if i not in stop4]
#
# arquivo5 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text5.txt", "r")
# text5 = arquivo5.read()
# stop5 = stopwords.words('english') + list(string.punctuation)
# tokens5 = [i for i in word_tokenize(text5.lower()) if i not in stop5]
#
# arquivo6 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text6.txt", "r")
# text6 = arquivo6.read()
# stop6 = stopwords.words('english') + list(string.punctuation)
# tokens6 = [i for i in word_tokenize(text6.lower()) if i not in stop6]
#
# arquivo7 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text7.txt", "r")
# text7 = arquivo7.read()
# stop7 = stopwords.words('english') + list(string.punctuation)
# tokens7 = [i for i in word_tokenize(text7.lower()) if i not in stop7]
#
# arquivo8 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text8.txt", "r")
# text8 = arquivo8.read()
# stop8 = stopwords.words('english') + list(string.punctuation)
# tokens8 = [i for i in word_tokenize(text8.lower()) if i not in stop8]
#
# arquivo9 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text9.txt", "r")
# text9 = arquivo9.read()
# stop9 = stopwords.words('english') + list(string.punctuation)
# tokens9 = [i for i in word_tokenize(text9.lower()) if i not in stop9]
#
# arquivo10 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text10.txt", "r")
# text10 = arquivo10.read()
# stop10 = stopwords.words('english') + list(string.punctuation)
# tokens10 = [i for i in word_tokenize(text10.lower()) if i not in stop10]
#
# arquivo11 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text11.txt", "r")
# text11 = arquivo11.read()
# stop11 = stopwords.words('english') + list(string.punctuation)
# tokens11 = [i for i in word_tokenize(text11.lower()) if i not in stop11]
#
# arquivo12 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text12.txt", "r")
# text12 = arquivo12.read()
# stop12 = stopwords.words('english') + list(string.punctuation)
# tokens12 = [i for i in word_tokenize(text12.lower()) if i not in stop12]
#
# arquivo13 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text13.txt", "r")
# text13 = arquivo13.read()
# stop13 = stopwords.words('english') + list(string.punctuation)
# tokens13 = [i for i in word_tokenize(text13.lower()) if i not in stop13]
#
# arquivo14 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text14.txt", "r")
# text14 = arquivo14.read()
# stop14 = stopwords.words('english') + list(string.punctuation)
# tokens14 = [i for i in word_tokenize(text14.lower()) if i not in stop14]
#
# arquivo15 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text15.txt", "r")
# text15 = arquivo15.read()
# stop15 = stopwords.words('english') + list(string.punctuation)
# tokens15 = [i for i in word_tokenize(text15.lower()) if i not in stop15]
#
# arquivo16 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text16.txt", "r")
# text16 = arquivo16.read()
# stop16 = stopwords.words('english') + list(string.punctuation)
# tokens16 = [i for i in word_tokenize(text16.lower()) if i not in stop16]
#
# arquivo17 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text17.txt", "r")
# text17 = arquivo17.read()
# stop17 = stopwords.words('english') + list(string.punctuation)
# tokens17 = [i for i in word_tokenize(text17.lower()) if i not in stop17]
#
# arquivo18 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text18.txt", "r")
# text18 = arquivo18.read()
# stop18 = stopwords.words('english') + list(string.punctuation)
# tokens18 = [i for i in word_tokenize(text18.lower()) if i not in stop18]
#
# arquivo19 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text19.txt", "r")
# text19 = arquivo19.read()
# stop19 = stopwords.words('english') + list(string.punctuation)
# tokens19 = [i for i in word_tokenize(text19.lower()) if i not in stop19]
#
# arquivo20 = open("/home/gnbettoni/PycharmProjects/tfidf_pattern/colecao_pubmed/text20.txt", "r")
# text20 = arquivo20.read()
# stop20 = stopwords.words('english') + list(string.punctuation)
# tokens20 = [i for i in word_tokenize(text20.lower()) if i not in stop20]

print "\n >>> Ending of pre-processing!"


def tf(word, doc):
    all_num = 0;
    for key in doc:
        all_num = all_num + len(key.split())
    word_num = 0
    for key in doc:
        if (key == word):
            word_num = word_num + 1
    return  word_num/all_num

def idf(word, doc_list):
    all_num = len(doc_list)
    word_count = 0
    for doc in doc_list:
        if word in doc:
            word_count+=1
    return log(all_num/word_count)

def tfidf(word, doc, doc_list):
    score = tf(word,doc)*(word, doc_list)
    return score

def similarity(list_final):
    print "Text 1: "
    print list_final[0]
    print "Text 2: "
    print list_final[1]
    print "Text 3: "
    print list_final[2]
    # just for tests
    # print "Text 4: "
    # print list_final[3]
    # print "Text 5: "
    # print list_final[4]
    # print "Text 6: "
    # print list_final[5]
    # print "Text 7: "
    # print list_final[6]
    # print "Text 8: "
    # print list_final[7]
    # print "Text 9: "
    # print list_final[8]
    # print "Text 10: "
    # print list_final[9]
    # print "Text 11: "
    # print list_final[10]
    # print "Text 12: "
    # print list_final[11]
    # print "Text 13: "
    # print list_final[12]
    # print "Text 14: "
    # print list_final[13]
    # print "Text 15: "
    # print list_final[14]
    # print "Text 16: "
    # print list_final[15]
    # print "Text 17: "
    # print list_final[16]
    # print "Text 18: "
    # print list_final[17]
    # print "Text 19: "
    # print list_final[18]
    # print "Text 20: "
    # print list_final[19]

    dp = float(dot(list_final[0], list_final[1], list_final[2]))
    np = float((norm(list_final[0])) * (norm(list_final[1])) * (norm(list_final[2])))

    #just for tests
    # dp = float(dot(list_final[0], list_final[1], list_final[2], list_final[3], list_final[4], list_final[5], list_final[6],
    #                list_final[7], list_final[8], list_final[9], list_final[10], list_final[11], list_final[12], list_final[13],
    #                list_final[14], list_final[15], list_final[16], list_final[17], list_final[18], list_final[19]))
    # np = float((norm(list_final[0])) * (norm(list_final[1])) * (norm(list_final[2])) * (norm(list_final[3])) * (norm(list_final[4]))
    #            * (norm(list_final[5])) * (norm(list_final[6])) * (norm(list_final[7])) * (norm(list_final[8])) * (norm(list_final[9]))
    #            * (norm(list_final[10])) * (norm(list_final[11])) * (norm(list_final[12])) * (norm(list_final[13])) * (norm(list_final[14]))
    #            * (norm(list_final[15])) * (norm(list_final[16])) * (norm(list_final[17])) * (norm(list_final[18])) * (norm(list_final[19]))
    #            * (norm(list_final[20])) )
    if (np == 0):
        np = 1
    print "Similarity: %s" % float(dp / np)

if __name__ == "__main__":

    doc1 = tokens1
    doc2 = tokens2
    doc3 = tokens3
    #just for tests
    # doc4 = tokens4
    # doc5 = tokens5
    # doc6 = tokens6
    # doc7 = tokens7
    # doc8 = tokens8
    # doc9 = tokens9
    # doc10 = tokens10
    # doc11 = tokens11
    # doc12 = tokens12
    # doc13 = tokens13
    # doc14 = tokens14
    # doc15 = tokens15
    # doc16 = tokens16
    # doc17 = tokens17
    # doc18 = tokens18
    # doc19 = tokens19
    # doc20 = tokens20


    list_final = []
    #test
    doc_list = [doc1, doc2, doc3]
    # correct list
    # doc_list=[doc1, doc2, doc3, doc4, doc5, doc6, doc7, doc8, doc9, doc10, doc11, doc12, doc13, doc14, doc15, doc16, doc17, doc18, doc19, doc20]
    i = 1
    for doc in doc_list:
        list_similarity = []
        for word in doc:
            score = tfidf(word,doc,doc_list)
            list_similarity.append(score)
        list_final.append(list_similarity)
        i+=1
    similarity(list_final)



