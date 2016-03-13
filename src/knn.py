import csv
import operator

from metricas import distancia_manhattan


def knn_1element(metric, k, elementToclassify):
    kElementos = []

    with open('data/_train.csv', 'rb') as f:
        setofTrain = csv.reader(f)
        next(setofTrain)

        for line in setofTrain:
            clase = int(line[0])
            element = map(int, line[1:])

            info_elem = { 'clase': clase, 'distancia': distancia_manhattan(elementToclassify, element) }

            if (len(kElementos) < k):
                kElementos.append(info_elem)
                kElementos.sort(key = operator.itemgetter('distancia'))
            else:
                if (info_elem['distancia'] < kElementos[k-1]['distancia']):
                    kElementos[k-1] = info_elem
                    kElementos.sort(key = operator.itemgetter('distancia'))

        cantidadXclase = [0] * 10

        for info_elem in kElementos:
            cantidadXclase[info_elem['clase']] += 1


        indiceClaseMayor = 0
        cantidadMayor = 0
        for i in range(0, len(cantidadXclase)):
            if (cantidadXclase[i] > cantidadMayor):
                cantidadMayor = cantidadXclase[i]
                indiceClaseMayor = i

        print(indiceClaseMayor)