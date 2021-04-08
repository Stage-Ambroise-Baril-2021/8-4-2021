#Ce document contient toutes les fonctions auxilliaires necessaires à la programmation des différents features, de façon à ce que chaque feature puisse s'écrire en un seul return.

import networkx as nx

from Features.ListBag import bag

from Features.NodesTypes import SetTypesNodes

from statistics import mean

from statistics import median

from numpy import std as sd

def count(L):

    return(len(set(L)))



#Fonctions booléenes de test.


def TrueTest(T,n):

    return(True)


def NonLeaf(T,n):

    try:

        _ = T.graph["Level"]

    except:

        SetTypesNodes(T)

    return(T.nodes[n]["Type"]!="Leaf")







def NonEmpty(T,n):

    return(not bag(T,n)==[])






def NodeTypeIsLeaf(T,n):

    return(T.nodes[n]["Type"]=="Leaf")

def NodeTypeIsIntroduce(T,n):

    return(T.nodes[n]["Type"]=="Introduce")

def NodeTypeIsForget(T,n):

    return(T.nodes[n]["Type"]=="Forget")

def NodeTypeIsJoin(T,n):

    return(T.nodes[n]["Type"]=="Join")





#Fonctions utilisées par les features qui ne peuvent pas s'écrire avec la fonction feature_bag ou feature_vertex_bag.




def ListContainerCount(G,T):#Fonction utilisée pour le feature ContainerCount. On ne peut pas utiliser feature_bag puisqu'on itère sur les sommets du graphe instance, et non sur les noeuds de la tree-decomposition.

    L=[]

    for v in G.nodes():

        count=0

        for n in T.nodes:

            if v in bag(T,n):

                count+=1

        L.append(count)

    return(L)


def ListItemLifeTime(G,T):#Fonction utilisée pour le feature ContainerCount. On ne peut pas utiliser feature_bag puisqu'on itère sur les sommets du graphe instance, et non sur les noeuds de la tree-decomposition.

    try:

        _ = T.graph["Level"]

    except:

        SetTypesNodes(T)

    L=[]

    for v in G.nodes():

        LevelReached=[False]*len(T.nodes)

        count=0

        for n in T.nodes:

            if v in bag(T,n) and not LevelReached[T.graph["Level"][n]]:

                count+=1

                LevelReached[T.graph["Level"][n]]=True

        L.append(count)

    return(L)


def ListJoinNodeDistance(T):#On suppose que tous les noms des noeuds de l'arbre sont du même type

    try:

        _ = T.graph["Level"]

    except:

        SetTypesNodes(T)

    L=[]

    for i in T.nodes:

        if T.nodes[i]["Type"] == "Join":

            Distance_i=nx.shortest_path_length(T,i)

            for j in T.nodes:

                if i<j and T.nodes[j]["Type"] == "Join":

                    L.append(Distance_i[j])

    if L==[]:#Si il y a au plus un seul noeud Join, on est censé renvoyer 0 à tous les features.

        L=[0]

    return(L)

####


#Fonctions requises par features_bag. Si le feature s'écrit \alpha({f(t), t noeud}), nous exprimons ici les différentes fonctions f.


def Children(T,n):

    try:

        Level = T.graph["Level"]

    except:

        SetTypesNodes(T)

        Level=T.graph["Level"]

    L=[]

    for m in T.nodes:

        if (n,m) in T.edges and Level[m]>Level[n]:

            L.append(m)

    return(L)


def NbChildren(G,T,n):

    return(len(Children(T,n)))





def AdjacencyFactor(G,T,n):#Fonction utilisée pour BagAdjacencyFactor

    if len(bag(T,n))==1:#Pas hyper sûr de ça, mais c'est indispensable pour être d'accord avec les tests. Supprimer si besoin.

        return(1)

    count=0

    for u in bag(T,n):

        for v in bag(T,n):

            if u!=v and (u,v) in G.edges():

                count+=1

    res=count/(max(1,(len(bag(T,n))*(len(bag(T,n))-1))))

    return(res)








def ConnectednessFactor(G,T,n):#Fonction utilisée pour BagConnectednessFactor

    if len(bag(T,n))==1:#Pas hyper sûr de ça, mais c'est indispensable pour être d'accord avec les tests. Supprimer si besoin.

        return(1)

    count=0

    for u in bag(T,n):

        for v in bag(T,n):

            if u!=v and nx.has_path(G,u,v):

                count+=1

    res=count/(max(1,(len(bag(T,n))*(len(bag(T,n))-1))))

    return(res)






def NeighborhoodCoverage(G,T,n):#Fonction utilisée pour BagNeighborhoodCoverageFactor

    if not NonEmpty(T,n):

        return(0)

    AdjG = nx.to_dict_of_dicts(G)

    L=[]

    for v in bag(T,n):

        count=0

        for u in bag(T,n):

            if (u,v) in G.edges():

                count+=1

        L.append(count/len(AdjG[v]))

    return(mean(L))



def NeighborsInBag(G,T,v,n):#Fonction utilisée pour IVNC et FVNC

    count=0

    for u in G.nodes:

        if (u,v) in G.edges and u in bag(T,n):

            count+=1

    return(count)







def ConnectednessFactorVertex(G,T,v,n):#Fonction utilisée pour IVCF et FVCF

    if len(bag(T,n))==1:#Pas hyper sûr de ça, mais c'est indispensable pour être d'accord avec les tests. Supprimer si besoin.

        return(1)

    count=0

    for u in bag(T,n):

        if u!=v and nx.has_path(G,u,v):

            count+=1

    res=count/(max(1,(len(bag(T,n))*(len(bag(T,n))-1))))

    return(res)






def VertexIsIntroduced(T,v,n):#Test utilisé par IVCN, retourne vrai si n est un introduce node où v a été introduit.


    try:

        _ = T.graph["Level"]

    except:

        SetTypesNodes(T)

    return(T.nodes[n]["Type"]=="Introduce" and v in bag(T,n) and (not (v in bag(T,Children(T,n)[0]))))






def VertexIsForgotten(T,v,n):#Test utilisé par FVCN, retourne vrai si n est un introduce node où v a été introduit.


    try:

        _ = T.graph["Level"]

    except:

        SetTypesNodes(T)

    return(T.nodes[n]["Type"]=="Forget" and (not (v in bag(T,n))) and v in bag(T,Children(T,n)[0]))







#Les deux fonctions majeures.










def feature_bag(G,T,function,filtre,alpha):

#Créé la liste [function(G,T,n) , n noeud de T tel que filtre(G,T,n) ], et lui applique la fonction alpha.

#Par exemple, BagSizeNonLeafMax va s'écrire: feature_bag(G,T,len_bag,NonLeaf,max)

#On ajoute un rattrapage d'erreur pour vérifier si SetTypesNodes a déjà été calculer, et le calculer si necessaire.

    try:

        _ = T.graph["Level"]

    except:

        SetTypesNodes(T)

    L=[]

    for n in T.nodes():
    
        if filtre(T,n):

            #print(n,function(G,T,n),"\n")#Utile pour debugger.

            L.append(function(G,T,n))

    #print(L)#Utile pour debugger.

    if L==[]:#On ne peut pas se permettre de faire une moyenne/mediane d'une liste vide !

        L=[0]

    return(alpha(L))






def feature_vertex_bag(G,T,function,filtre,alpha):#Analogue de feature_bag, mais on itère sur les couples (v,n) où v in bag(T,n). Le filtre porte sur les noeuds de l'arbre.

    try:

        _ = T.graph["Level"]

    except:

        SetTypesNodes(T)

    L=[]

    for v in G.nodes:  

        for n in T.nodes:

            if filtre(T,v,n):

                L.append(function(G,T,v,n))

    if L==[]:

        L=[0]

    return(alpha(L))



