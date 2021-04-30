import os

from WriteMatrix import WriteMatrix

from numpy import std as sd

from random import shuffle

from random import randint

from importlib import reload

from statistics import mean

from statistics import median

Graphs=["Graph-"+str(i) for i in range(1,197)]

ListRanks=[]

RanksOccur=[0]*10

for k in range(50):

    print(k)

    shuffle(Graphs)

    Training=list(Graphs[:100])

    WriteMatrix(Training)

    if k==0:

        import KRGPipelinesRank

    for n in range(101,111):

        path="Training/"+Graphs[n]+'/'

        if k!=0 and n==101:

            rank=reload(KRGPipelinesRank).KRGPipelinesRank(path)

        else:

            rank=KRGPipelinesRank.KRGPipelinesRank(path)

        print(rank,'\n')

        ListRanks.append(rank)

        RanksOccur[rank-1]+=1

    os.remove("MatricesTraining/X.csv")

    os.remove("MatricesTraining/Y.csv")


print('\n')

print("Rang moyen:",mean(ListRanks),'\n')

print("Rang médian:",median(ListRanks),'\n')

print("Ecart type:,",sd(ListRanks),'\n')

print("Occurence des rangs;",RanksOccur,'\n')
