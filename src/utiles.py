from PIL import Image

def imprimir_imagen(list, size, nombre_imagen):
    im = Image.new('L', size)
    im.putdata(list)
    im.save(nombre_imagen)