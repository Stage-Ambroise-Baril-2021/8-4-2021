#Ce script génère dix décompositions arboresentes aléatoires des instances décrites par la variable i, calcule leurs features, et les stockent dans les matrices X et Y.

for i in $(seq 10 99)

do

cd /home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Grakel/Training

mkdir Graph-$i

for j in $(seq 11 20)

do

    #Génerer une décomposition arborescente avec DFLAT.

    cd /home/ambroise/Bureau/DFLAT/TR/applications/dflat

    start_time=$(date +%s.%3N)

    ./dflat -p ../../encodings/dflat/3col/encoding.lp --tables -n normalized -e vertex -e edge --graphml-out tree0.ml < /home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Instances_Multiples/Instances/instance_n20_p0.10_0$i.lp

    end_time=$(date +%s.%3N)

    realtime=$(echo "scale=3; $end_time - $start_time" | bc)

    #Calculer les labels

    mv "tree0.ml" "/home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Grakel/tree$i-$j.ml"

    cd /home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Grakel

    python3 TreeToGraphml.py tree$i-$j.ml

    python3 NodesLabel.py tree$i-$j.ml $realtime

    #Déplacer les TD dans le dossier Training.

    mv "tree$i-$j.ml" "/home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Grakel/Training/Graph-$i/tree$i-$j.ml"

done

done
