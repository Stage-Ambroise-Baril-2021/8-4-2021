#Ce script génère dix décompositions arboresentes aléatoires des instances décrites par la variable i, calcule leurs features, et les stockent dans les matrices X et Y.

for i in $(seq 61 80)

do

for j in $(seq 1 10)

do

    #Génerer une décomposition arborescente avec DFLAT.

    cd /home/ambroise/Bureau/DFLAT/TR/applications/dflat

    start_time=$(date +%s.%3N)

    ./dflat -p ../../encodings/dflat/3col/encoding.lp --tables -n normalized -e vertex -e edge --graphml-out tree0.ml < /home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Instances_Multiples/Instances/instance_n20_p0.10_0$i.lp

    end_time=$(date +%s.%3N)

    realtime=$(echo "scale=3; $end_time - $start_time" | bc)

    #Calculer les featues

    mv "tree0.ml" "/home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Instances_Multiples/Conversion+Features+Time/tree$i-$j.ml"

    cd /home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Instances_Multiples/Conversion+Features+Time

    cp "/home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Instances_Multiples/Instances/instance_n20_p0.10_0$i.lp" "instance_n20_p0.10_0$i.lp"

    python3 Conversion+Features+Time.py instance_n20_p0.10_0$i.lp tree$i-$j.ml $realtime

    #Déplacer les Features.csv dans le dossier Training.

    mv "Features_tree$i-$j.ml.csv" "/home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Instances_Multiples/Training/Features_tree$i-$j.ml.csv"

    mv "tree$i-$j.ml" "/home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Instances_Multiples/Training/tree$i-$j.ml"

    rm "instance_n20_p0.10_0$i.lp"

done

done

cd "/home/ambroise/Bureau/Python_ML_Sklearn/Test_DFLAT/Instances_Multiples"

python3 Training.py
