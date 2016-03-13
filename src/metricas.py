#Punto es una lista de integers

def distancia_minkowsky(puntoA, puntoB, p):
    sumatoria = 0
    for i in range(0,len(puntoA)):
        sumatoria += abs(puntoA[i]-puntoB[i])**p
    return sumatoria**(1/p)

def distancia_manhattan(puntoA, puntoB):
    return distancia_minkowsky(puntoA,puntoB, 1)

def distancia_euclideana(puntoA, puntoB):
    return distancia_minkowsky(puntoA, puntoB, 2)

def distancia_hamming(puntoA, puntoB):

    return 0

def distancia_mahalanobis(puntoA, puntoB):

     return 0