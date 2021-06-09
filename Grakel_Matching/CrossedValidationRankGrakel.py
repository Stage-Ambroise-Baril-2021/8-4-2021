import os

from numpy import std as sd

from random import shuffle

from random import randint

from statistics import mean

from statistics import median

from AdjLabelsTime import *

from WriteList import WriteList

from importlib import reload

Graphs=["Graph-"+str(i) for i in range(1,198)]

ListRanks=[]

RanksOccur=[0]*20

for k in range(50):

    print("Itération "+str(k)+":")

    shuffle(Graphs)

    TrainingSet=list(Graphs[:50])


    WriteList(TrainingSet)


    if k==0:

        import GrakelRank

    for n in range(50,60):

        path="Training/"+Graphs[n]+'/'

        if k!=0 and n==50:

            rank=reload(GrakelRank).GrakelRank(path)

        else:

            rank=GrakelRank.GrakelRank(path)

        print("Son rang réel est:")

        print(rank,'\n')

        ListRanks.append(rank)

        RanksOccur[rank-1]+=1



print('\n')

print("Rang moyen:",mean(ListRanks),'\n')

print("Rang médian:",median(ListRanks),'\n')

print("Ecart type:",sd(ListRanks),'\n')

print("Occurence des rangs:",RanksOccur,'\n')
