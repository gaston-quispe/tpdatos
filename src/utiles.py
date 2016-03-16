import csv
from PIL import Image

def imprimir_imagen(list, size, nombre_imagen):
    im = Image.new('L', size)
    im.putdata(list)
    im.save(nombre_imagen)

def imprimir_imagenes_test(testcsv):
    with open(testcsv, 'rb') as f:
        setDeTest = csv.reader(f)
        next(setDeTest)

        numeroLinea = 0
        for line in setDeTest:
            elementoAimprimir = map(int, line)
            imprimir_imagen(elementoAimprimir, (28,28), "salidas/linea-" + str(numeroLinea) + ".png")
            numeroLinea += 1