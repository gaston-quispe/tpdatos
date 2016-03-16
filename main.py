import time
from src.knn import knn
from src.metricas import distancia_manhattan
from src.utiles import imprimir_imagenes_test

imprimir_imagenes_test("data/_test10elem.csv")
start = time.time()
listaclases = knn("data/_train100elem.csv", "data/_test10elem.csv", distancia_manhattan, 3)
end = time.time()

print end - start
print listaclases