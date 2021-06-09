import networkx as nx

from grakel import Graph

import os

from AdjLabelsTime import *

from WriteMatrix import WriteMatrix

def Training(TrainingSet):

    X=[]

    Y=[]

    for folder in TrainingSet:

        for root, dirs, files in os.walk("Training/"+folder):#Construction de X et de Y.

            for name in files:

                path="Training/"+folder+'/'+name

                G=Graph( initialization_object=Adj(path), node_labels=Node_Labels(path) )

                X.append(G)

                Y.append(Time(path))

    WriteMatrix(X,Y)
