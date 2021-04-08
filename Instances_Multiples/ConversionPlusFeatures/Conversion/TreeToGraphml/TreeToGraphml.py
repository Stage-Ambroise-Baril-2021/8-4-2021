#Script qui modifie un fichier renvoyé par DFLAT représentant une décomposition arborescente, en une version lisible par networkx.

#Ici, on définit une fonction qui fait la conversion.

import os

def TreeToGraphml(Non_du_document_à_modifier):

    doc=open(Non_du_document_à_modifier,'r')
    aux=open("Auxilliaire.ml",'x')

    for line in doc:

        aux.write(line.replace("<key id=\"bag\" for=\"node\"/>","<key id=\"d0\" for=\"node\" attr.name=\"bag\" attr.type=\"string\" />"))

    doc.close()
    aux.close()

    aux=open("Auxilliaire.ml",'r')
    doc=open(Non_du_document_à_modifier,'w')

    for line in aux:

        doc.write(line.replace("<data key=\"bag\">","<data key=\"d0\"> "))

    aux.close()
    doc.close()

    os.remove("Auxilliaire.ml")
