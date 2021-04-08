#Ce script demande un graphe sous forme d'instance utilisée par DFLAT, une décomposition arborescente générée par DFLAT, ainsi que le temps mis par l'algo DP pour résoudre l'instance. Il les convertit en format exploitable par networkx et écrit dans un fichier CSV leurs features, et le temps mis.

#Si ce script est appliqué à un graphe/décomposition arborescente déjà lisible par networkx, il ne sera pas modifié par l'étape de conversion.

from Conversion.GraphToGraphml.GraphToGraphml import GraphToGraphml as GraphToGraphml

from Conversion.TreeToGraphml.TreeToGraphml import TreeToGraphml as TreeToGraphml

from Features import Features

import sys

Fichier_G=sys.argv[1]

Fichier_T=sys.argv[2]

Time=sys.argv[3]

GraphToGraphml(Fichier_G)

TreeToGraphml(Fichier_T)

Features.Features(Fichier_G,Fichier_T,Time)
