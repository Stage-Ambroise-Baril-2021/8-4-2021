#Commentaire obsolète.

#Ce script utilise les fichiers .csv du dossier ToCompare, les ordonne selon le temps réellement mis, puis, dans un second temps, essaye sans regarder le temps mis, de le prédire avec SKLEARN. On regarde ensuite le rang réel de la tree decomposition ayant reçu la meilleure prédiction. On regarde le temps gagné par rapport à si on avait choisi une tree decomposition aléatoire.

import os

import networkx as nx

from random import randint

from sklearn.svm import SVC

from AdjLabelsTime import *

from grakel import GraphKernel

from ReadList import ReadList

sp_kernel = GraphKernel(kernel="shortest_path",normalize=True)

from grakel import Graph

from sklearn.svm import SVC

#Test 5 sans kernel='precomputed'

clf = SVC(kernel='precomputed')

#A la place de SVC, utiliser SVR.





print("Training")

TrainingSet=ReadList("ListTraining/TrainingSet.csv")

X=[]

Y=[]

for folder in TrainingSet:

    #Recherche du graphe

    for root, dirs, files in os.walk("Training/"+folder+"/Instance"):#Construction de X et de Y.

        for graphname in files:

            path="Training/"+folder+"/Instance/"+graphname

            G=nx.read_graphml(path)

            n_graph=len(G.nodes)

    #Recherche des TD

    for root, dirs, files in os.walk("Training/"+folder):#Construction de X et de Y.

        for name in files:

            if name[:5]!="graph":

                path="Training/"+folder+'/'+name

                #print(path)

                #print(Node_Labels(n_graph,path))

                T=Graph( initialization_object=Adj(path), node_labels=Node_Labels(n_graph,path) )

                X.append(T)

                Y.append(Class(path))





K_train=sp_kernel.fit_transform(X)

clf.fit(K_train,Y)

#print(K_train)


def GrakelRank(path):

    ListReal=[]

    for root, dirs, files in os.walk(path):

        for name in files:

            if name.endswith((".ml")) and name[:4]=="tree":

                ListReal.append( (Rank(path+name),name) )

    ListReal.sort()
    
    
    print("ListReal:\n")

    print(ListReal,'\n')
    
    
    #On essaye ensuite de faire des prédiction sans regarder le temps réel.


    ###


    for root, dirs, files in os.walk(path+"/Instance/"):

        for graphname in files:

            pathG=path+"/Instance/"+graphname

            G=nx.read_graphml(pathG)

            n_graph=len(G.nodes)
    
    
    
    ListPredict=[]

    for root, dirs, files in os.walk(path):
    
        for name in files:
    
            if name.endswith((".ml")) and name[:4]=="tree":
    
                X0=Graph( Adj(path+name), Node_Labels(n_graph,path+name) )
    
                NormX0=sp_kernel.transform([X0])
    
                ListPredict.append((clf.predict(NormX0)[0],name))
    
    ListPredict.sort()
    
    print("ListPredict:\n")    

    print(ListPredict,'\n')
    
    
    PredictedBestTree=ListPredict[0][1]
    
    print("J'ai choisi "+PredictedBestTree)
    
    #PredictedBestTree est la tree decomposition dont on prévoit le meilleur rank. On le retrouve dans la liste des rank réels, et on regarde son rang rél. On essaye aussi d'évaluer l'amélioration par rapport à une TD prise aléatoirement.


    for i in range(len(ListReal)):
    
        if ListReal[i][1] == PredictedBestTree:

            rank=i+1

            return(rank)
    
            #print("Rang: \n"+str(i+1)+'/'+str(len(ListReal))+'\n')
    
            #RandomTreeIndex=randint(0,len(ListReal)-1)

            #RandomTime=ListReal[RandomTreeIndex][0]
    
            #Improvement=RandomTime-ListReal[i][0]
    
            #print("Amélioration par rapport à random: \n"+str(Improvement))
    
            #return(Improvement,RandomTime)
