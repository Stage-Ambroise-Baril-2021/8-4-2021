#Définit une fonction qui écrit dans un fichier nommé ResultatFeatures.csv les valeurs des Features appliqué au graphe et à sa décomposition arborescente passés en argument.

from Features.FeaturesFunctions import *

def Features(Nom_du_fichier_contenant_G,Nom_du_fichier_contenant_T,Time):

    G=nx.read_graphml(Nom_du_fichier_contenant_G)
    T=nx.read_graphml(Nom_du_fichier_contenant_T)

    Tabular=open("Features_"+Nom_du_fichier_contenant_T+".csv",'x')

    Tabular.write("Feature" + "," "Valeur\n")

    for i in range(142):

        Tabular.write(all_features_names[i] + "," + str(all_features[i](G,T)) + "\n")

    Tabular.write("Time,"+str(float(Time)))

    Tabular.close()
