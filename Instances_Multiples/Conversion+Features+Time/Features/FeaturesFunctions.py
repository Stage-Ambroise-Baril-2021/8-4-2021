#Tout marche bien, sauf les features qui font intervenir une division par |\chi_i|*(|\chi_i|-1), dont la définition est trop peu claire. Le problème vient des bags de taille 1. La proportion d'arêtes présente parmis les arêtes possibles est mal définie (le nombre d'arête possible étant 0). La formule choisit la convention 0 dans ce cas, tandis que le résultat de l'exemple oblige la convention à être 1.

import networkx as nx

from Features.FeaturesAux import *




#all_functions=[BagSizeCount, BagSizeMax, BagSizeMin, BagSizeMean, BagSizeMedian, BagSizeSd, BagSizeNonLeafCount, BagSizeNonLeafMax, BagSizeNonLeafMin, BagSizeNonLeafMean, BagSizeNonLeafMedian, BagSizeNonLeafSd, BagSizeNonEmptyCount, BagSizeNonEmptyMax, BagSizeNonEmptyMin, BagSizeNonEmptyMean, BagSizeNonEmptyMedian, BagSizeNonEmptySd, CumulativeBagSize, DecompositionOverheadRatio, ContainerCountMax, ContainerCountMin, ContainerCountMean, ContainerCountMedian, ContainerCountSd, ItemLifeTimeMax, ItemLifeTimeMin, ItemLifeTimeMean, ItemLifeTimeMedian, ItemLifeTimeSd, NodesDepthMax, NodeDepthMin, NodeDepthMean, NodeDepthMedian, NodeDepthSd, NodeDepthNonLeafMax, NodeDepthNonLeafMin, NodeDepthNonLeafMean, NodeDepthNonLeafMedian, NodeDepthNonLeafSd, NodeDepthNonEmptyMax, NodeDepthNonEmptyMin, NodeDepthNonEmptyMean, NodeDepthNonEmptyMedian, NodeDepthNonEmptySd, PercentageLeaf, PercentageIntroduce, PercentageForget, PercentageJoin, BagSizeLeafCount, BagSizeLeafMax, BagSizeLeafMin, BagSizeLeafMean, BagSizeLeafMedian, BagSizeLeafSd, BagSizeIntroduceCount, BagSizeIntroduceMax, BagSizeIntroduceMin, BagSizeIntroduceMean, BagSizeIntroduceMedian, BagSizeIntroduceSd, BagSizeForgetCount, BagSizeForgetMax, BagSizeForgetMin, BagSizeForgetMean, BagSizeForgetMedian, BagSizeForgetSd, BagSizeJoinCount, BagSizeJoinMax, BagSizeJoinMin, BagSizeJoinMean, BagSizeJoinMedian, BagSizeJoinSd, CumulativeBagSizeLeaf, CumulativeBagSizeIntroduce, CumulativeBagSizeForget, CumulativeBagSizeJoin, DepthLeafMax, DepthLeafMin, DepthLeafMean, DepthLeafMedian, DepthLeafSd, DepthIntroduceMax, DepthIntroduceMin, DepthIntroduceMean, DepthIntroduceMedian, DepthIntroduceSd, DepthForgetMax, DepthForgetMin, DepthForgetMean, DepthForgetMedian, DepthForgetSd, DepthJoinMax, DepthJoinMin, DepthJoinMean, DepthJoinMedian, DepthJoinSd, JoinNodeDistanceMax, JoinNodeDistanceMin, JoinNodeDistanceMean, JoinNodeDistanceMedian, JoinNodeDistanceSd, BranchingFactorMax, BranchingFactorMin, BranchingFactorMean, BranchingFactorMedian, BranchingFactorSd, BAFMax, BAFMin, BAFMean, BAFMedian, BAFSd, BCFMax, BCFMin, BCFMean, BCFMedian, BCFSd, BNCFMax, BNCFMin, BNCFMean, BNCFMedian, BNCFSd, IVNCMax, IVNCMin, IVNCMean, IVNCMedian, IVNCSd, FVNCMax, FVNCMin, FVNCMean, FVNCMedian, FVNCSd, IVCFMax, IVCFMin, IVCFMean, IVCFMedian, IVCFSd, FVCFMax, FVCFMin, FVCFMean, FVCFMedian, FVCFSd]





#all_functions_names=['BagSizeCount', 'BagSizeMax', 'BagSizeMin', 'BagSizeMean', 'BagSizeMedian', 'BagSizeSd', 'BagSizeNonLeafCount', 'BagSizeNonLeafMax', 'BagSizeNonLeafMin', 'BagSizeNonLeafMean', 'BagSizeNonLeafMedian', 'BagSizeNonLeafSd', 'BagSizeNonEmptyCount', 'BagSizeNonEmptyMax', 'BagSizeNonEmptyMin', 'BagSizeNonEmptyMean', 'BagSizeNonEmptyMedian', 'BagSizeNonEmptySd', 'CumulativeBagSize', 'DecompositionOverheadRatio', 'ContainerCountMax', 'ContainerCountMin', 'ContainerCountMean', 'ContainerCountMedian', 'ContainerCountSd', 'ItemLifeTimeMax', 'ItemLifeTimeMin', 'ItemLifeTimeMean', 'ItemLifeTimeMedian', 'ItemLifeTimeSd', 'NodesDepthMax', 'NodeDepthMin', 'NodeDepthMean', 'NodeDepthMedian', 'NodeDepthSd', 'NodeDepthNonLeafMax', 'NodeDepthNonLeafMin', 'NodeDepthNonLeafMean', 'NodeDepthNonLeafMedian', 'NodeDepthNonLeafSd', 'NodeDepthNonEmptyMax', 'NodeDepthNonEmptyMin', 'NodeDepthNonEmptyMean', 'NodeDepthNonEmptyMedian', 'NodeDepthNonEmptySd', 'PercentageLeaf', 'PercentageIntroduce', 'PercentageForget', 'PercentageJoin', 'BagSizeLeafCount', 'BagSizeLeafMax', 'BagSizeLeafMin', 'BagSizeLeafMean', 'BagSizeLeafMedian', 'BagSizeLeafSd', 'BagSizeIntroduceCount', 'BagSizeIntroduceMax', 'BagSizeIntroduceMin', 'BagSizeIntroduceMean', 'BagSizeIntroduceMedian', 'BagSizeIntroduceSd', 'BagSizeForgetCount', 'BagSizeForgetMax', 'BagSizeForgetMin', 'BagSizeForgetMean', 'BagSizeForgetMedian', 'BagSizeForgetSd', 'BagSizeJoinCount', 'BagSizeJoinMax', 'BagSizeJoinMin', 'BagSizeJoinMean', 'BagSizeJoinMedian', 'BagSizeJoinSd', 'CumulativeBagSizeLeaf', 'CumulativeBagSizeIntroduce', 'CumulativeBagSizeForget', 'CumulativeBagSizeJoin', 'DepthLeafMax', 'DepthLeafMin', 'DepthLeafMean', 'DepthLeafMedian', 'DepthLeafSd', 'DepthIntroduceMax', 'DepthIntroduceMin', 'DepthIntroduceMean', 'DepthIntroduceMedian', 'DepthIntroduceSd', 'DepthForgetMax', 'DepthForgetMin', 'DepthForgetMean', 'DepthForgetMedian', 'DepthForgetSd', 'DepthJoinMax', 'DepthJoinMin', 'DepthJoinMean', 'DepthJoinMedian', 'DepthJoinSd', 'JoinNodeDistanceMax', 'JoinNodeDistanceMin', 'JoinNodeDistanceMean', 'JoinNodeDistanceMedian', 'JoinNodeDistanceSd', 'BranchingFactorMax', 'BranchingFactorMin', 'BranchingFactorMean', 'BranchingFactorMedian', 'BranchingFactorSd', 'BAFMax', 'BAFMin', 'BAFMean', 'BAFMedian', 'BAFSd', 'BCFMax', 'BCFMin', 'BCFMean', 'BCFMedian', 'BCFSd', 'BNCFMax', 'BNCFMin', 'BNCFMean', 'BNCFMedian', 'BNCFSd', 'IVNCMax', 'IVNCMin', 'IVNCMean', 'IVNCMedian', 'IVNCSd', 'FVNCMax', 'FVNCMin', 'FVNCMean', 'FVNCMedian', 'FVNCSd', 'IVCFMax', 'IVCFMin', 'IVCFMean', 'IVCFMedian', 'IVCFSd', 'FVCFMax', 'FVCFMin', 'FVCFMean', 'FVCFMedian', 'FVCFSd']






#Decomposition Size Features

def BagSizeCount(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , TrueTest ,count))

def BagSizeMax(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , TrueTest ,max))

def BagSizeMin(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , TrueTest ,min))

def BagSizeMean(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , TrueTest ,mean))

def BagSizeMedian(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , TrueTest ,median))

def BagSizeSd(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , TrueTest ,sd))

def BagSizeNonLeafCount(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonLeaf ,count))

def BagSizeNonLeafMax(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonLeaf ,max))

def BagSizeNonLeafMin(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonLeaf ,min))

def BagSizeNonLeafMean(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonLeaf ,mean))

def BagSizeNonLeafMedian(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonLeaf ,median))

def BagSizeNonLeafSd(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonLeaf ,sd))

def BagSizeNonEmptyCount(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonEmpty ,count))

def BagSizeNonEmptyMax(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonEmpty ,max))

def BagSizeNonEmptyMin(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonEmpty ,min))

def BagSizeNonEmptyMean(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonEmpty ,mean))

def BagSizeNonEmptyMedian(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonEmpty ,median))

def BagSizeNonEmptySd(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NonEmpty ,sd))

def CumulativeBagSize(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , TrueTest ,sum))

def DecompositionOverheadRatio(G,T):

    return(CumulativeBagSize(G,T)/(len(G.nodes())))

def ContainerCountMax(G,T):

    return(max(ListContainerCount(G,T)))

def ContainerCountMin(G,T):

    return(min(ListContainerCount(G,T)))

def ContainerCountMean(G,T):

    return(mean(ListContainerCount(G,T)))

def ContainerCountMedian(G,T):

    return(median(ListContainerCount(G,T)))

def ContainerCountSd(G,T):

    return(sd(ListContainerCount(G,T)))

def ItemLifeTimeMax(G,T):

    return(max(ListItemLifeTime(G,T)))

def ItemLifeTimeMin(G,T):

    return(min(ListItemLifeTime(G,T)))

def ItemLifeTimeMean(G,T):

    return(mean(ListItemLifeTime(G,T)))

def ItemLifeTimeMedian(G,T):

    return(median(ListItemLifeTime(G,T)))

def ItemLifeTimeSd(G,T):

    return(sd(ListItemLifeTime(G,T)))

def NodesDepthMax(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , TrueTest ,max)))

def NodeDepthMin(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , TrueTest ,min)))

def NodeDepthMean(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , TrueTest ,mean)))

def NodeDepthMedian(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , TrueTest ,median)))

def NodeDepthSd(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , TrueTest ,sd)))

def NodeDepthNonLeafMax(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonLeaf ,max)))

def NodeDepthNonLeafMin(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonLeaf ,min)))

def NodeDepthNonLeafMean(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonLeaf ,mean)))

def NodeDepthNonLeafMedian(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonLeaf ,median)))

def NodeDepthNonLeafSd(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonLeaf ,sd)))

def NodeDepthNonEmptyMax(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonEmpty ,max)))

def NodeDepthNonEmptyMin(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonEmpty ,min)))

def NodeDepthNonEmptyMean(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonEmpty ,mean)))

def NodeDepthNonEmptyMedian(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonEmpty ,median)))

def NodeDepthNonEmptySd(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NonEmpty ,sd)))



#Nodes_types_features



def PercentageLeaf(G,T):

    return(feature_bag(G,T,lambda G,T,n: 1 , NodeTypeIsLeaf , sum)/len(T.nodes))

def PercentageIntroduce(G,T):

    return(feature_bag(G,T,lambda G,T,n: 1 , NodeTypeIsIntroduce , sum)/len(T.nodes))

def PercentageForget(G,T):

    return(feature_bag(G,T,lambda G,T,n: 1 , NodeTypeIsForget , sum)/len(T.nodes))

def PercentageJoin(G,T):

    return(feature_bag(G,T,lambda G,T,n: 1 , NodeTypeIsJoin , sum)/len(T.nodes))

def BagSizeLeafCount(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsLeaf ,count))

def BagSizeLeafMax(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsLeaf ,max))

def BagSizeLeafMin(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsLeaf ,min))

def BagSizeLeafMean(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsLeaf ,mean))

def BagSizeLeafMedian(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsLeaf ,median))

def BagSizeLeafSd(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsLeaf ,sd))

def BagSizeIntroduceCount(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsIntroduce ,count))

def BagSizeIntroduceMax(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsIntroduce ,max))

def BagSizeIntroduceMin(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsIntroduce ,min))

def BagSizeIntroduceMean(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsIntroduce ,mean))

def BagSizeIntroduceMedian(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsIntroduce ,median))

def BagSizeIntroduceSd(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsIntroduce ,sd))

def BagSizeForgetCount(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsForget ,count))

def BagSizeForgetMax(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsForget ,max))

def BagSizeForgetMin(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsForget ,min))

def BagSizeForgetMean(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsForget ,mean))

def BagSizeForgetMedian(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsForget ,median))

def BagSizeForgetSd(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsForget ,sd))

def BagSizeJoinCount(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsJoin ,count))

def BagSizeJoinMax(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsJoin ,max))

def BagSizeJoinMin(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsJoin ,min))

def BagSizeJoinMean(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsJoin ,mean))

def BagSizeJoinMedian(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsJoin ,median))

def BagSizeJoinSd(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsJoin ,sd))

def CumulativeBagSizeLeaf(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsLeaf ,sum))

def CumulativeBagSizeIntroduce(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsIntroduce ,sum))

def CumulativeBagSizeForget(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsForget ,sum))

def CumulativeBagSizeJoin(G,T):

    return(feature_bag(G,T,lambda G,T,n : len(bag(T,n)) , NodeTypeIsJoin ,sum))

def DepthLeafMax(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsLeaf ,max)))

def DepthLeafMin(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsLeaf ,min)))

def DepthLeafMean(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsLeaf ,mean)))

def DepthLeafMedian(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsLeaf ,median)))

def DepthLeafSd(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsLeaf ,sd)))

def DepthIntroduceMax(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsIntroduce ,max)))

def DepthIntroduceMin(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsIntroduce ,min)))

def DepthIntroduceMean(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsIntroduce ,mean)))

def DepthIntroduceMedian(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsIntroduce ,median)))

def DepthIntroduceSd(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsIntroduce ,sd)))

def DepthForgetMax(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsForget ,max)))

def DepthForgetMin(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsForget ,min)))

def DepthForgetMean(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsForget ,mean)))

def DepthForgetMedian(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsForget ,median)))

def DepthForgetSd(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsForget ,sd)))

def DepthJoinMax(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsJoin ,max)))

def DepthJoinMin(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsJoin ,min)))

def DepthJoinMean(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsJoin ,mean)))

def DepthJoinMedian(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsJoin ,median)))

def DepthJoinSd(G,T):

    return((feature_bag(G,T,lambda G,T,n: T.graph["Level"][n] , NodeTypeIsJoin ,sd)))

def JoinNodeDistanceMax(G,T):

    return(max(ListJoinNodeDistance(T)))

def JoinNodeDistanceMin(G,T):

    return(min(ListJoinNodeDistance(T)))

def JoinNodeDistanceMean(G,T):

    return(mean(ListJoinNodeDistance(T)))

def JoinNodeDistanceMedian(G,T):

    return(median(ListJoinNodeDistance(T)))

def JoinNodeDistanceSd(G,T):

    return(sd(ListJoinNodeDistance(T)))



#Structural Features



def BranchingFactorMax(G,T):

    return(feature_bag(G,T,NbChildren, TrueTest , max))

def BranchingFactorMin(G,T):

    return(feature_bag(G,T,NbChildren, TrueTest , min))

def BranchingFactorMean(G,T):

    return(feature_bag(G,T,NbChildren, TrueTest , mean))

def BranchingFactorMedian(G,T):

    return(feature_bag(G,T,NbChildren, TrueTest , median))

def BranchingFactorSd(G,T):

    return(feature_bag(G,T,NbChildren, TrueTest , sd))

#Pour être d'accord avec les exemples, il ne faut pas suivre la formule et considérer que si un bag n'a qu'un seul sommet, la proportion est égale à 1.

def BAFMax(G,T):

    return(feature_bag(G,T,AdjacencyFactor, TrueTest , max))

def BAFMin(G,T):

    return(feature_bag(G,T,AdjacencyFactor, TrueTest , min))

def BAFMean(G,T):

    return(feature_bag(G,T,AdjacencyFactor, TrueTest , mean))

def BAFMedian(G,T):

    return(feature_bag(G,T,AdjacencyFactor, TrueTest , median))

def BAFSd(G,T):

    return(feature_bag(G,T,AdjacencyFactor, TrueTest , sd))

def BCFMax(G,T):

    return(feature_bag(G,T,ConnectednessFactor, TrueTest , max))

def BCFMin(G,T):

    return(feature_bag(G,T,ConnectednessFactor, TrueTest , min))

def BCFMean(G,T):

    return(feature_bag(G,T,ConnectednessFactor, TrueTest , mean))

def BCFMedian(G,T):

    return(feature_bag(G,T,ConnectednessFactor, TrueTest , median))

def BCFSd(G,T):

    return(feature_bag(G,T,ConnectednessFactor, TrueTest , sd))

def BNCFMax(G,T):

    return(feature_bag(G,T,NeighborhoodCoverage, TrueTest ,max))

def BNCFMin(G,T):

    return(feature_bag(G,T,NeighborhoodCoverage, TrueTest , min))

def BNCFMean(G,T):

    return(feature_bag(G,T,NeighborhoodCoverage, TrueTest , mean))

def BNCFMedian(G,T):

    return(feature_bag(G,T,NeighborhoodCoverage, TrueTest , median))

def BNCFSd(G,T):

    return(feature_bag(G,T,NeighborhoodCoverage, TrueTest , sd))

def IVNCMax(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsIntroduced, max))

def IVNCMin(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsIntroduced, min))

def IVNCMean(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsIntroduced, mean))

def IVNCMedian(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsIntroduced, median))

def IVNCSd(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsIntroduced, sd))

def FVNCMax(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsForgotten, max))

def FVNCMin(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsForgotten, min))

def FVNCMean(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsForgotten, mean))

def FVNCMedian(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsForgotten, median))

def FVNCSd(G,T):

    return(feature_vertex_bag(G,T,NeighborsInBag, VertexIsForgotten, sd))

#Définition de IVCF pas claire du tout.

def IVCFMax(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsIntroduced, max))

def IVCFMin(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsIntroduced, min))

def IVCFMean(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsIntroduced, mean))

def IVCFMedian(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsIntroduced, median))

def IVCFSd(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsIntroduced, sd))

def FVCFMax(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsForgotten, max))

def FVCFMin(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsForgotten, min))

def FVCFMean(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsForgotten, mean))

def FVCFMedian(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsForgotten, median))

def FVCFSd(G,T):

    return(feature_vertex_bag(G,T,ConnectednessFactorVertex, VertexIsForgotten, sd))





#Liste de tous les features, et de tous leurs noms.







all_features=[BagSizeCount, BagSizeMax, BagSizeMin, BagSizeMean, BagSizeMedian, BagSizeSd, BagSizeNonLeafCount, BagSizeNonLeafMax, BagSizeNonLeafMin, BagSizeNonLeafMean, BagSizeNonLeafMedian, BagSizeNonLeafSd, BagSizeNonEmptyCount, BagSizeNonEmptyMax, BagSizeNonEmptyMin, BagSizeNonEmptyMean, BagSizeNonEmptyMedian, BagSizeNonEmptySd, CumulativeBagSize, DecompositionOverheadRatio, ContainerCountMax, ContainerCountMin, ContainerCountMean, ContainerCountMedian, ContainerCountSd, ItemLifeTimeMax, ItemLifeTimeMin, ItemLifeTimeMean, ItemLifeTimeMedian, ItemLifeTimeSd, NodesDepthMax, NodeDepthMin, NodeDepthMean, NodeDepthMedian, NodeDepthSd, NodeDepthNonLeafMax, NodeDepthNonLeafMin, NodeDepthNonLeafMean, NodeDepthNonLeafMedian, NodeDepthNonLeafSd, NodeDepthNonEmptyMax, NodeDepthNonEmptyMin, NodeDepthNonEmptyMean, NodeDepthNonEmptyMedian, NodeDepthNonEmptySd, PercentageLeaf, PercentageIntroduce, PercentageForget, PercentageJoin, BagSizeLeafCount, BagSizeLeafMax, BagSizeLeafMin, BagSizeLeafMean, BagSizeLeafMedian, BagSizeLeafSd, BagSizeIntroduceCount, BagSizeIntroduceMax, BagSizeIntroduceMin, BagSizeIntroduceMean, BagSizeIntroduceMedian, BagSizeIntroduceSd, BagSizeForgetCount, BagSizeForgetMax, BagSizeForgetMin, BagSizeForgetMean, BagSizeForgetMedian, BagSizeForgetSd, BagSizeJoinCount, BagSizeJoinMax, BagSizeJoinMin, BagSizeJoinMean, BagSizeJoinMedian, BagSizeJoinSd, CumulativeBagSizeLeaf, CumulativeBagSizeIntroduce, CumulativeBagSizeForget, CumulativeBagSizeJoin, DepthLeafMax, DepthLeafMin, DepthLeafMean, DepthLeafMedian, DepthLeafSd, DepthIntroduceMax, DepthIntroduceMin, DepthIntroduceMean, DepthIntroduceMedian, DepthIntroduceSd, DepthForgetMax, DepthForgetMin, DepthForgetMean, DepthForgetMedian, DepthForgetSd, DepthJoinMax, DepthJoinMin, DepthJoinMean, DepthJoinMedian, DepthJoinSd, JoinNodeDistanceMax, JoinNodeDistanceMin, JoinNodeDistanceMean, JoinNodeDistanceMedian, JoinNodeDistanceSd, BranchingFactorMax, BranchingFactorMin, BranchingFactorMean, BranchingFactorMedian, BranchingFactorSd, BAFMax, BAFMin, BAFMean, BAFMedian, BAFSd, BCFMax, BCFMin, BCFMean, BCFMedian, BCFSd, BNCFMax, BNCFMin, BNCFMean, BNCFMedian, BNCFSd, IVNCMax, IVNCMin, IVNCMean, IVNCMedian, IVNCSd, FVNCMax, FVNCMin, FVNCMean, FVNCMedian, FVNCSd, IVCFMax, IVCFMin, IVCFMean, IVCFMedian, IVCFSd, FVCFMax, FVCFMin, FVCFMean, FVCFMedian, FVCFSd]


all_features_names=['BagSizeCount', 'BagSizeMax', 'BagSizeMin', 'BagSizeMean', 'BagSizeMedian', 'BagSizeSd', 'BagSizeNonLeafCount', 'BagSizeNonLeafMax', 'BagSizeNonLeafMin', 'BagSizeNonLeafMean', 'BagSizeNonLeafMedian', 'BagSizeNonLeafSd', 'BagSizeNonEmptyCount', 'BagSizeNonEmptyMax', 'BagSizeNonEmptyMin', 'BagSizeNonEmptyMean', 'BagSizeNonEmptyMedian', 'BagSizeNonEmptySd', 'CumulativeBagSize', 'DecompositionOverheadRatio', 'ContainerCountMax', 'ContainerCountMin', 'ContainerCountMean', 'ContainerCountMedian', 'ContainerCountSd', 'ItemLifeTimeMax', 'ItemLifeTimeMin', 'ItemLifeTimeMean', 'ItemLifeTimeMedian', 'ItemLifeTimeSd', 'NodesDepthMax', 'NodeDepthMin', 'NodeDepthMean', 'NodeDepthMedian', 'NodeDepthSd', 'NodeDepthNonLeafMax', 'NodeDepthNonLeafMin', 'NodeDepthNonLeafMean', 'NodeDepthNonLeafMedian', 'NodeDepthNonLeafSd', 'NodeDepthNonEmptyMax', 'NodeDepthNonEmptyMin', 'NodeDepthNonEmptyMean', 'NodeDepthNonEmptyMedian', 'NodeDepthNonEmptySd', 'PercentageLeaf', 'PercentageIntroduce', 'PercentageForget', 'PercentageJoin', 'BagSizeLeafCount', 'BagSizeLeafMax', 'BagSizeLeafMin', 'BagSizeLeafMean', 'BagSizeLeafMedian', 'BagSizeLeafSd', 'BagSizeIntroduceCount', 'BagSizeIntroduceMax', 'BagSizeIntroduceMin', 'BagSizeIntroduceMean', 'BagSizeIntroduceMedian', 'BagSizeIntroduceSd', 'BagSizeForgetCount', 'BagSizeForgetMax', 'BagSizeForgetMin', 'BagSizeForgetMean', 'BagSizeForgetMedian', 'BagSizeForgetSd', 'BagSizeJoinCount', 'BagSizeJoinMax', 'BagSizeJoinMin', 'BagSizeJoinMean', 'BagSizeJoinMedian', 'BagSizeJoinSd', 'CumulativeBagSizeLeaf', 'CumulativeBagSizeIntroduce', 'CumulativeBagSizeForget', 'CumulativeBagSizeJoin', 'DepthLeafMax', 'DepthLeafMin', 'DepthLeafMean', 'DepthLeafMedian', 'DepthLeafSd', 'DepthIntroduceMax', 'DepthIntroduceMin', 'DepthIntroduceMean', 'DepthIntroduceMedian', 'DepthIntroduceSd', 'DepthForgetMax', 'DepthForgetMin', 'DepthForgetMean', 'DepthForgetMedian', 'DepthForgetSd', 'DepthJoinMax', 'DepthJoinMin', 'DepthJoinMean', 'DepthJoinMedian', 'DepthJoinSd', 'JoinNodeDistanceMax', 'JoinNodeDistanceMin', 'JoinNodeDistanceMean', 'JoinNodeDistanceMedian', 'JoinNodeDistanceSd', 'BranchingFactorMax', 'BranchingFactorMin', 'BranchingFactorMean', 'BranchingFactorMedian', 'BranchingFactorSd', 'BAFMax', 'BAFMin', 'BAFMean', 'BAFMedian', 'BAFSd', 'BCFMax', 'BCFMin', 'BCFMean', 'BCFMedian', 'BCFSd', 'BNCFMax', 'BNCFMin', 'BNCFMean', 'BNCFMedian', 'BNCFSd', 'IVNCMax', 'IVNCMin', 'IVNCMean', 'IVNCMedian', 'IVNCSd', 'FVNCMax', 'FVNCMin', 'FVNCMean', 'FVNCMedian', 'FVNCSd', 'IVCFMax', 'IVCFMin', 'IVCFMean', 'IVCFMedian', 'IVCFSd', 'FVCFMax', 'FVCFMin', 'FVCFMean', 'FVCFMedian', 'FVCFSd']
