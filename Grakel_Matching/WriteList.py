import os

import csv;




def WriteList(List):

    os.chdir("ListTraining/")

    doc=open("TrainingSet.csv",'x')

    for i in range(len(List)):

        doc.write(str(List[i]))

        doc.write(str('\n'))

    doc.close()

    os.chdir("../")

