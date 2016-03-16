import time
from src.knn import knn
from src.metricas import distancia_manhattan
from src.utiles import imprimir_imagenes_test
from src.forward_editing import forward_editing

imprimir_imagenes_test("data/_test10elem.csv")
start = time.time()
listaclases = knn("data/_train100elem.csv", "data/_test10elem.csv", distancia_manhattan, 3)
end = time.time()

print end - start
print listaclases

print "Prueba editing"
print "Lista de prototipos: "
prototipos = forward_editing("data/_train100elem.csv", distancia_manhattan, 3)
cantidad_prototipos = 0
for i in prototipos:
    print i
    cantidad_prototipos += 1

print "Cantidad de prototipos: " + str(cantidad_prototipos)