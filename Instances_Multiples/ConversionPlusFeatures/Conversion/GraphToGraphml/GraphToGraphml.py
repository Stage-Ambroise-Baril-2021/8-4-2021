#Script qui modifie un fichier comme utilisé par DFLAT représentant une instance (par exemple le fichier instance_n20_p0.10_001.lp ), en une version lisible par networkx.

#Ici, on définit une fonction qui modifie le document passé en argument.

import os


def IndiceVirgule(line=str):#Renvoie l'indice correspondant à la première virgule de la chaine de caractères line.

    n=len(line)

    for i in range(n):

        if line[i]==",":

            return(i)



def GraphToGraphml(Non_du_document_à_modifier):

    doc=open(Non_du_document_à_modifier,'r')
    aux=open("Auxilliaire.ml",'x')

    aux.write("<?xml version='1.0' encoding='utf-8'?>\n<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">\n  <graph edgedefault=\"undirected\">\n\n")

    for line in doc:

        if "xml" in line:

            os.remove("Auxilliaire.ml")

            return(None)

        if len(line)>=6 and line[:6]=="vertex":

            vertex=line[7:-3]

            aux.write("    <node id=\""+vertex+"\" />\n\n")

        if len(line)>=4 and line[:4]=="edge":

            indexcoma=IndiceVirgule(line)

            vertex1=line[5:indexcoma]

            vertex2=line[indexcoma+1:-3]

            aux.write("    <edge source=\""+vertex1+"\" target=\""+vertex2+"\" />\n\n")


    aux.write("  </graph>\n</graphml>")

    doc.close()
    aux.close()

    aux=open("Auxilliaire.ml",'r')
    doc=open(Non_du_document_à_modifier,'w')

    for line in aux:

        doc.write(line)

    aux.close()
    doc.close()

    os.remove("Auxilliaire.ml")
