import metricas
from knn import knn


def grid_search(traincsv, clases, cantidad_observaciones):
    mejor_precision = 0; mejor_k = 0; mejor_metrica = 0
    lista_metricas = [metricas.distancia_euclideana(), metricas.distancia_manhattan(), metricas.distancia_hamming()]
    for k in range(0,100):
        for metrica in lista_metricas:
            prediccionKnn = knn(traincsv, clases, metrica, k, )
            precision = sum(prediccionKnn == clases)/cantidad_observaciones
            if(precision > mejor_precision):
                mejor_precision = precision
                mejor_k = k
                mejor_metrica = metrica

    return mejor_k, mejor_metrica

