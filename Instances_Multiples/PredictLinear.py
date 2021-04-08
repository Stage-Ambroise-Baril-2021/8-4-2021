#Ce script de machine Learning apprend des fichiers .csv du dossier Training, et de leurs "scores" stockés dans Time.csv (Machine Learning supervisé), et fait une prédiction pour Features_tree0.

from sklearn import linear_model

from sklearn.preprocessing import StandardScaler

from ReadMatrices import *

from ConversionPlusFeatures.ConversionPlusFeatures import ConversionPlusFeatures

reg = linear_model.LinearRegression()

import os

import sys

import csv;

instance0=sys.argv[1]

tree0=sys.argv[2]

###


#Début de la partie apprentissage.





#On remplit la matrice X.




X=ReadX("MatricesTraining/X.csv")




scaler = StandardScaler()

scaler.fit(X)




NormX=scaler.transform(X)





#On remplit la matrice Y.



Y=ReadY("MatricesTraining/Y.csv")



#Comme précisé dans l'article, on effectue la regression avec la forme normalisée de X, mais on laisse Y tel quel.



reg.fit (NormX, Y)




#Fin de la partie d'apprentissage.


###







#Ecriture des features;



ConversionPlusFeatures(instance0,tree0)





###





#Début de la partie de prédiction.






#On n'oublie pas de normaliser FeaturesTree0 ! On lui applique la même transformation qui a servi à normaliser la matrice X.





X0=ReadX0("Features_"+tree0+".csv")


NormX0=scaler.transform([X0])


os.remove("Features_"+tree0+".csv")

print(reg.predict(NormX0)[0])






#Conseils : Utiliser les pipelines.
