import os

import csv;


all_features_names=['BagSizeCount', 'BagSizeMax', 'BagSizeMin', 'BagSizeMean', 'BagSizeMedian', 'BagSizeSd', 'BagSizeNonLeafCount', 'BagSizeNonLeafMax', 'BagSizeNonLeafMin', 'BagSizeNonLeafMean', 'BagSizeNonLeafMedian', 'BagSizeNonLeafSd', 'BagSizeNonEmptyCount', 'BagSizeNonEmptyMax', 'BagSizeNonEmptyMin', 'BagSizeNonEmptyMean', 'BagSizeNonEmptyMedian', 'BagSizeNonEmptySd', 'CumulativeBagSize', 'DecompositionOverheadRatio', 'ContainerCountMax', 'ContainerCountMin', 'ContainerCountMean', 'ContainerCountMedian', 'ContainerCountSd', 'ItemLifeTimeMax', 'ItemLifeTimeMin', 'ItemLifeTimeMean', 'ItemLifeTimeMedian', 'ItemLifeTimeSd', 'NodesDepthMax', 'NodeDepthMin', 'NodeDepthMean', 'NodeDepthMedian', 'NodeDepthSd', 'NodeDepthNonLeafMax', 'NodeDepthNonLeafMin', 'NodeDepthNonLeafMean', 'NodeDepthNonLeafMedian', 'NodeDepthNonLeafSd', 'NodeDepthNonEmptyMax', 'NodeDepthNonEmptyMin', 'NodeDepthNonEmptyMean', 'NodeDepthNonEmptyMedian', 'NodeDepthNonEmptySd', 'PercentageLeaf', 'PercentageIntroduce', 'PercentageForget', 'PercentageJoin', 'BagSizeLeafCount', 'BagSizeLeafMax', 'BagSizeLeafMin', 'BagSizeLeafMean', 'BagSizeLeafMedian', 'BagSizeLeafSd', 'BagSizeIntroduceCount', 'BagSizeIntroduceMax', 'BagSizeIntroduceMin', 'BagSizeIntroduceMean', 'BagSizeIntroduceMedian', 'BagSizeIntroduceSd', 'BagSizeForgetCount', 'BagSizeForgetMax', 'BagSizeForgetMin', 'BagSizeForgetMean', 'BagSizeForgetMedian', 'BagSizeForgetSd', 'BagSizeJoinCount', 'BagSizeJoinMax', 'BagSizeJoinMin', 'BagSizeJoinMean', 'BagSizeJoinMedian', 'BagSizeJoinSd', 'CumulativeBagSizeLeaf', 'CumulativeBagSizeIntroduce', 'CumulativeBagSizeForget', 'CumulativeBagSizeJoin', 'DepthLeafMax', 'DepthLeafMin', 'DepthLeafMean', 'DepthLeafMedian', 'DepthLeafSd', 'DepthIntroduceMax', 'DepthIntroduceMin', 'DepthIntroduceMean', 'DepthIntroduceMedian', 'DepthIntroduceSd', 'DepthForgetMax', 'DepthForgetMin', 'DepthForgetMean', 'DepthForgetMedian', 'DepthForgetSd', 'DepthJoinMax', 'DepthJoinMin', 'DepthJoinMean', 'DepthJoinMedian', 'DepthJoinSd', 'JoinNodeDistanceMax', 'JoinNodeDistanceMin', 'JoinNodeDistanceMean', 'JoinNodeDistanceMedian', 'JoinNodeDistanceSd', 'BranchingFactorMax', 'BranchingFactorMin', 'BranchingFactorMean', 'BranchingFactorMedian', 'BranchingFactorSd', 'BAFMax', 'BAFMin', 'BAFMean', 'BAFMedian', 'BAFSd', 'BCFMax', 'BCFMin', 'BCFMean', 'BCFMedian', 'BCFSd', 'BNCFMax', 'BNCFMin', 'BNCFMean', 'BNCFMedian', 'BNCFSd', 'IVNCMax', 'IVNCMin', 'IVNCMean', 'IVNCMedian', 'IVNCSd', 'FVNCMax', 'FVNCMin', 'FVNCMean', 'FVNCMedian', 'FVNCSd', 'IVCFMax', 'IVCFMin', 'IVCFMean', 'IVCFMedian', 'IVCFSd', 'FVCFMax', 'FVCFMin', 'FVCFMean', 'FVCFMedian', 'FVCFSd']



def WriteMatrix(ListFolders):

    X=[["Features"]+all_features_names]

    Y=[["Tree Decompositions","Times"]]

    for folder in ListFolders:

        #print(folder)

        for root, dirs, files in os.walk("Training/"+folder):#Construction de X et de Y.

            for name in files:

                #print(name)

                if name.endswith((".csv")):

                    X_row_i=[name]

                    Y_row_i=[name]

                    doc=open("Training/"+folder+'/'+name,'r')

                    ReadFeatures_i=csv.reader(doc)

                    for Features_j in ReadFeatures_i:

                        if Features_j[1] != "Valeur" and Features_j[0] != "Time":

                            X_row_i.append(float(Features_j[1]))

                        if Features_j[0] == "Time":

                            Y_row_i.append(float(Features_j[1]))

                    X.append(X_row_i)

                    Y.append(Y_row_i)

                    doc.close()



    #print(X)

    #print(Y)


    os.chdir("MatricesTraining")


    docX=open("X.csv",'x')

    docY=open("Y.csv",'x')



    n=len(X)

    m=len(X[0])

    for i in range(n):

        for j in range(m):

            docX.write(str(X[i][j]))

            if j<m-1:

                docX.write(',')

        docX.write('\n')


    for i in range(n):

        docY.write(Y[i][0]+',')

        docY.write(str(Y[i][1])+'\n')

    
    docX.close()
    
    docY.close()

    os.chdir("../")

