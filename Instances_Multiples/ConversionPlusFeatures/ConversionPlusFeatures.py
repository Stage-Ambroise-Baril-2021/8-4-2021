#Ce script demande un graphe sous forme d'instance utilisée par DFLAT, ainsi qu'une décomposition arborescente générée par DFLAT. Il les convertit en format exploitable par networkx et écrit dans un fichier CSV leurs features.

#Ici, on définit une fonction.

#Si ce script est appliqué à un graphe/décomposition arborescente déjà lisible par networkx, il ne sera pas modifié par l'étape de conversion.

from ConversionPlusFeatures.Conversion.GraphToGraphml.GraphToGraphml import GraphToGraphml as GraphToGraphml

from ConversionPlusFeatures.Conversion.TreeToGraphml.TreeToGraphml import TreeToGraphml as TreeToGraphml

from ConversionPlusFeatures.Features import Features

def ConversionPlusFeatures(Fichier_G,Fichier_T):

    GraphToGraphml(Fichier_G)

    TreeToGraphml(Fichier_T)

    Features.Features(Fichier_G,Fichier_T)
