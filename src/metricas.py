#Punto es una lista de integers

def distancia_manhattan(puntoA, puntoB):
    resultado = 0
    for i in puntoA:
        resultado += abs(puntoA[i]-puntoB[i])
    return resultado


def distancia_hamming(puntoA, puntoB):

    return 0