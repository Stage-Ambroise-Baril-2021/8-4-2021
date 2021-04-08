#Ce script permet de lire un csv et d'en faire une matrice. Il y a une version pour la matrice X, une pour Y, et une pour l'instance de test.

import csv

def ReadX(pathX):

    docX=open(pathX,'r')

    readX=csv.reader(docX)

    X=[]

    i=0

    for read_row_X in readX:

        if i>0:

            row_X_i=[]

            for j in range(len(read_row_X)):

                if j>0:

                    row_X_i.append(float(read_row_X[j]))

            X.append(row_X_i)

        i=i+1

    docX.close()

    return(X)



def ReadY(pathY):

    docY=open(pathY,'r')

    readY=csv.reader(docY)

    Y=[]

    i=0

    for read_row_Y in readY:

        if i>0:

            Y.append(float(read_row_Y[1]))

        i=i+1

    docY.close()

    return(Y)



def ReadX0(pathX0):

    doc0=open(pathX0,'r')

    ReadFeatures_0=csv.reader(doc0)

    X0=[]

    j=0

    for Features_j in ReadFeatures_0:

        if Features_j[1] != "Valeur" and Features_j[0] != "Time":

            X0.append((float(Features_j[1])))

            j=j+1

    doc0.close()

    return(X0)

