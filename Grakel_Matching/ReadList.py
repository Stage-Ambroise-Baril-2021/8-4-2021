#Ce script permet de lire un csv et d'en faire une matrice. Il y a une version pour la matrice X, une pour Y, et une pour l'instance de test.

import csv

import os

def ReadList(path):

    doc=open(path,'r')

    read=csv.reader(doc)

    List=[]

    i=0

    for read_row in read:

        List.append(read_row[0])

    doc.close()

    os.remove(path)

    return(List)
