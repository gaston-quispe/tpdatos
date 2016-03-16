from src.metricas import distancia_euclideana
from src.metricas import distancia_manhattan
from src.metricas import distancia_hamming
from knn import knn


def grid_search(traincsv, test, clases, cantidad_observaciones):
    mejor_precision = 0; mejor_k = 0; mejor_metrica = 0
    lista_metricas = [distancia_manhattan, distancia_euclideana, distancia_hamming]

    for k in range(1,5):
        for metrica in lista_metricas:
            prediccionKnn = knn(traincsv, test, metrica, k)
            suma = 0
            for i in prediccionKnn:
                if(prediccionKnn[i] == clases[i]):
                    suma += 1

            precision = (suma*1.0)/cantidad_observaciones
            if(precision > mejor_precision):
                        mejor_precision = precision
                        mejor_k = k
                        mejor_metrica = metrica

    return mejor_k, mejor_metrica, mejor_precision

