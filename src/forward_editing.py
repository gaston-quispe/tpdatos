import csv
import knnV2

def bienClasificado(prediccion, clase):
    return prediccion == clase

def forward_editing(traincsv, metrica, k):
    setDePrototipos = []

    with open(traincsv, 'rb') as f:
            setDeEntrenamiento = csv.reader(f)
            next(setDeEntrenamiento)

            for line in setDeEntrenamiento:
                #Convierto el vector de strings a un vector de enteros
                element = map(int, line[0:])

                #El primer elemento de la linea es la clase
                clase = element[0]

                prediccion = knnV2.knn2_1element(setDePrototipos, metrica, k, element[1:])

                if(bienClasificado(prediccion, clase) == False):
                    setDePrototipos.append(element)
    return setDePrototipos