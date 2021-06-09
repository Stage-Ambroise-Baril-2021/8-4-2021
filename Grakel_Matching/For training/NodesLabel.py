#L'objectif est qu'après l'application à effet de bord SetLabelsNodes(T), les noeuds de T possèdent le feature "Label", dont la valeur pourra être "Leaf", "Join", ou "Introduce"+str(i) si le noeud est un Introduce node qui introduit le noeud i, et "Forget"+str(i) si le noeud est un Forget node qui oublie le noeud i. On suppose que la racine de T s'appelle "n1". SetLabelsNodes(T) renvoie l'erreur "Forme non normalisée" si il ne parvient pas à attribuer un type a au moins un noeud.

#Un graphe à qui SetLabelsNodes a déjà été appliqué aura en plus la liste des niveaux de ses sommets dans un attribut "Level". Cela permet en particulier de tester si un graphe a déjà reçu SetTypesNodes: on appelle T.graph["Level"], et si une erreur sort, on en déduit que SetLabelsNodes n'a jamais été appliqué.


import networkx as nx

import sys

pathT=sys.argv[1]

time=sys.argv[2]

from ListBag import bag

root="n1"

def LevelList(T):#

    return(nx.shortest_path_length(T,root))

def Fils(Level,AdjT,n):#Level=LevelList(T), AdjT=nx.to_dict_of_dicts(T)

    Res=[]

    for m in AdjT[n]:

        if Level[m]>Level[n]:

            Res.append(m)

    return(Res)

def SetLabelsNodes(T):

    Level=LevelList(T)

    T.graph["Level"]=Level

    AdjT=nx.to_dict_of_dicts(T)

    for n in T.nodes():

        fils_n=Fils(Level,AdjT,n)

        if fils_n==[]:

            T.nodes[n]["Label"]="Leaf"

        elif len(fils_n)==1 and set(bag(T,fils_n[0]))<=set(bag(T,n)) and len(bag(T,n))==len(bag(T,fils_n[0]))+1:

            T.nodes[n]["Label"]="Introduce "+str( list( set(bag(T,n)) - set(bag(T,fils_n[0])) )[0]  )

        elif len(fils_n)==1 and set(bag(T,n))<=set(bag(T,fils_n[0])) and len(bag(T,n))==len(bag(T,fils_n[0]))-1:

            T.nodes[n]["Label"]="Forget "+str( list( set(bag(T,fils_n[0]))  -  set(bag(T,n)) )[0]  )

        elif len(fils_n)==1:

            raise Exception("Forme non normalisée")

        else:

            for m in fils_n:

                if set(bag(T,n)) != set(bag(T,m)):

                    raise Exception("Forme non normalisée")

            T.nodes[n]["Label"]="Join"

    T.graph["Level"]="Level"

    T.graph["Time"]=time

T=nx.read_graphml(pathT)

SetLabelsNodes(T)

nx.write_graphml(T,pathT)

#for n in TestTree.nodes():

    #print(n)

    #print(TestTree.nodes[n]["Type"])

    #print("\n")










