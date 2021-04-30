#Ce script utilise les fichiers .csv du dossier ToCompare, les ordonne selon le temps réellement mis, puis, dans un second temps, essaye sans regarder le temps mis, de le prédire avec SKLEARN. On regarde ensuite le rang réel de la tree decomposition ayant reçu la meilleure prédiction. On regarde le temps gagné par rapport à si on avait choisi une tree decomposition aléatoire.

from sklearn.decomposition import PCA

from sklearn.pipeline import Pipeline

from sklearn.model_selection import GridSearchCV

import sys

#i=sys.argv[1]

#path="ToCompare/ToCompare"+str(i)+'/'

import os

import csv

from random import randint

from sklearn.kernel_ridge import KernelRidge

from sklearn.preprocessing import StandardScaler

from ReadMatrices import *











X=ReadX("MatricesTraining/X.csv")
    
    
scaler = StandardScaler()
    
scaler.fit(X)
    
NormX=scaler.transform(X)
    
    
    
Y=ReadY("MatricesTraining/Y.csv")
    
    
    
    
    
    
print("Pipelines")    
    
clf=KernelRidge()
    
    
# Define a pipeline to search for the best combination of PCA truncation
# and classifier regularization.
pca = PCA()
    
pipe = Pipeline(steps=[('pca', pca), ('clf', clf)])
    
# Parameters of pipelines can be set using ‘__’ separated parameter names:
param_grid = {
    'pca__n_components': [ 95, 115, 135],
    'clf__kernel': ["poly"],
    'clf__alpha': [0.9**n for n in range(5)],
}

search = GridSearchCV(pipe, param_grid, n_jobs=-1)
search.fit(NormX, Y)


#print(search.best_score_)

print(search.best_params_)


param=search.best_params_
    
alpha=param['clf__alpha']
    
kernel=param['clf__kernel']
    
    
clf=KernelRidge(alpha=alpha,kernel=kernel)
    
clf.fit(NormX,Y)

    
#Conseil: Changer grille de paramètre PCA, echelle log pour alpha. Changer, prendre degré 2,3,...
    
#Conseil: Utiliser aussi la Support Vector Regression







#On ordonne d'abord les tree decompositions selon leur temps réel dans la liste ListTime.

def KRGPipelinesRank(path):#KRGPipelines(path,RandomTreeIndex)

    ListReal=[]

    for root, dirs, files in os.walk(path):

        for name in files:

            if name.endswith((".csv")):

                doc=open(path+name,'r')

                ReadFeatures_i=csv.reader(doc)

                for Features_j in ReadFeatures_i:

                    if Features_j[0] == "Time":

                        ListReal.append((float(Features_j[1]),name))

                doc.close()

    ListReal.sort()
    
    
    #print(ListReal,'\n')
    
    
    #On essaye ensuite de faire des prédiction sans regarder le temps réel.
    
    


    
    
    
    
    
    ListPredict=[]
    
    for root, dirs, files in os.walk(path):
    
        for name in files:
    
            if name.endswith((".csv")):
    
                X0=ReadX0(path+name)
    
                NormX0=scaler.transform([X0])
    
                ListPredict.append((clf.predict(NormX0)[0],name))
    
    ListPredict.sort()
    
    
    #print(ListPredict,'\n')
    
    
    PredictedBestTree=ListPredict[0][1]
    
    #print("J'ai choisi "+PredictedBestTree+'\n')
    
    #PredictedBestTree est la tree decomposition dont on prévoit le meilleur temps. On le retrouve dans la liste des temps réels, et on regarde son rang. On essaye aussi d'évaluer l'amélioration par rapport à un arbre pris aléatoirement.


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
