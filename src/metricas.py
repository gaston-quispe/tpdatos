#Punto es una lista de integers

def distancia_minkowsky(puntoA, puntoB, p):
    sumatoria = 0
    longitud = len(puntoA)

    if(p == 0):
        for i in range(0,longitud):
            if(puntoA[i] != puntoB[i]):
                sumatoria += 1
        return sumatoria

    for i in range(0,longitud):
        sumatoria += abs(puntoA[i]-puntoB[i])**p
    return sumatoria**(1.0/p)

def distancia_manhattan(puntoA, puntoB):
    return distancia_minkowsky(puntoA,puntoB, 1)

def distancia_euclideana(puntoA, puntoB):
    return distancia_minkowsky(puntoA, puntoB, 2)

def distancia_hamming(puntoA, puntoB):
    return distancia_minkowsky(puntoA, puntoB, 0)

def distancia_mahalanobis(puntoA, puntoB):

    return 0

def norma_infinito(puntoA, puntoB):
    distancia = 0

    for i in range(0,len(puntoA)):
        diferencia = abs(puntoA[i]-puntoB[i])
        if(diferencia > distancia):
            distancia = diferencia
    return distancia