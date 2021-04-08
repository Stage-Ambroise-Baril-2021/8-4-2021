#L'objectif est de d'écrire la fonction "bag", qui permet de passer de la présentation des bags sous forme de str à la liste des sommets, plus exploitable.

import networkx as nx

def ListBag(bag=str):#Transforme "12, 3, 6" en ["12","3","6"]

    if bag==" ":#Cas bizarre d'un bag vide

        return([])

    b=bag+","#b="12, 3, 6,"

    l=b.split()#l=["12,", "3,", "6,"]

    L=[]

    for s in l:#Quand s="12," ; int(s[:-1])==12

        L.append( s[:-1] )

    return(L)

def bag(T,n):#bag(T,n) renvoie le bag correspondant au noeud nommé n, sous forme de liste

    return(ListBag(T.nodes[n]["bag"]))


#C'est fini, mais on fait des tests

#for n in Test.nodes():

    #print(n)

    #print(bag(Test,n))

    #print("\n")

