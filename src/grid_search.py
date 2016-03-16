import metricas
import knn


def grid_search(elementToclassify, cantidad_observaciones):
    mejor_precision = 0; mejor_k = 0; mejor_metrica = 0
    lista_metricas = [metricas.distancia_euclideana(), metricas.distancia_manhattan(), metricas.distancia_hamming()]
    for k in range(0,100):
        for metrica in lista_metricas:
            resultadoKnn = knn.knn_1element(metrica, k, elementToclassify)
            precision = sum(resultadoKnn)/cantidad_observaciones
            if(precision > mejor_precision):
                mejor_precision = precision
                mejor_k = k
                mejor_metrica = metrica

