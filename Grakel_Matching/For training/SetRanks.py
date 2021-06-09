import networkx as nx

from AdjLabelsTime import Time

import os

import sys

path=sys.argv[1]

ListReal=[]

for root, dirs, files in os.walk(path):

    for name in files:

        if name.endswith((".ml")):

            ListReal.append(   (   float( Time(path+name)  ) , name    )   )

ListReal.sort()

for i in range(len(ListReal)):

    name=ListReal[i][1]

    T=nx.read_graphml(path+name)

    T.graph["Rank"]=i+1

    nx.write_graphml(T,path+name)
