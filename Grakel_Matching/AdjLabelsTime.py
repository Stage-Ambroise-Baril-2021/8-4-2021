#Ce script définit les fonction necessaires pour que Grakel puisse exploiter les décompositions arborescentes avec leurs labels.

from random import randint

import networkx as nx

def Node_Labels(n_graph,path):

    T=nx.read_graphml(path)

    node_labels={}

    for n in T.nodes:

        try:

            if T.nodes[n]["Label"][:9]=="Introduce":

                node_labels[ n_graph+int(n[1:])-1 ]=("Introduce", len( T.nodes[n]["bag"].split() ) )

            elif T.nodes[n]["Label"][:6]=="Forget":

                node_labels[ n_graph+int(n[1:])-1 ]=("Forget", len( T.nodes[n]["bag"].split() ) )

            else:

                node_labels[ n_graph+int(n[1:])-1 ]=(T.nodes[n]["Label"], len( T.nodes[n]["bag"].split() ) )

        except:

            node_labels[ int(n) ]="Graph"

    return(node_labels)

def Adj(path):

    T=nx.read_graphml(path)

    return(nx.adjacency_matrix(T))

def Time(path):

    T=nx.read_graphml(path)

    return(T.graph["Time"])

def Rank(path):

    T=nx.read_graphml(path)

    return(T.graph["Rank"])

def Class(path):

    T=nx.read_graphml(path)

    return(T.graph["Rank"])
