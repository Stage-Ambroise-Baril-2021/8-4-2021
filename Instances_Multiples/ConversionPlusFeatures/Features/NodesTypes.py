#L'objectif est qu'après l'application à effet de bord SetTypesNodes(T), les noeuds de T possèdent le feature "Type", dont la valeur pourra être "Leaf", "Introduce", "Forget", ou "Join". On suppose que la racine de T s'appelle "n1". SetTypesNodes(T) renvoie l'erreur "Forme non normalisée" si il ne parvient pas à attribuer un type a au moins un noeud.

#Un graphe à qui SetTypesNodes a déjà été appliqué aura en plus la liste des niveaux de ses sommets dans un attribut "Level". Cela permet en particulier de tester si un graphe a déjà reçu SetTypesNodes: on appelle T.graph["Level"], et si une erreur sort, on en déduit que SetTypesNodes n'a jamais été appliqué.


import networkx as nx

from ConversionPlusFeatures.Features.ListBag import bag

root="n1"

def LevelList(T):#

    return(nx.shortest_path_length(T,root))

def Fils(Level,AdjT,n):#Level=LevelList(T), AdjT=nx.to_dict_of_dicts(T)

    Res=[]

    for m in AdjT[n]:

        if Level[m]>Level[n]:

            Res.append(m)

    return(Res)

def SetTypesNodes(T):

    Level=LevelList(T)

    T.graph["Level"]=Level

    AdjT=nx.to_dict_of_dicts(T)

    for n in T.nodes():

        fils_n=Fils(Level,AdjT,n)

        if fils_n==[]:

            T.nodes[n]["Type"]="Leaf"

        elif len(fils_n)==1 and set(bag(T,fils_n[0]))<=set(bag(T,n)) and len(bag(T,n))==len(bag(T,fils_n[0]))+1:

            T.nodes[n]["Type"]="Introduce"

        elif len(fils_n)==1 and set(bag(T,n))<=set(bag(T,fils_n[0])) and len(bag(T,n))==len(bag(T,fils_n[0]))-1:

            T.nodes[n]["Type"]="Forget"

        elif len(fils_n)==1:

            raise Exception("Forme non normalisée")

        else:

            for m in fils_n:

                if set(bag(T,n)) != set(bag(T,m)):

                    raise Exception("Forme non normalisée")

            T.nodes[n]["Type"]="Join"


#for n in TestTree.nodes():

    #print(n)

    #print(TestTree.nodes[n]["Type"])

    #print("\n")










