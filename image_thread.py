from PIL import Image
import os
from settings import get
import multiprocessing
from functools import partial

# https://stackoverflow.com/questions/5442910/how-to-use-multiprocessing-pool-map-with-multiple-arguments

ruteOrigin = get('origin')
ruteDestiny = get('destino')
listOrigin = os.listdir(ruteOrigin)
listDestino = os.listdir(ruteDestiny)


def createNewDestiny(listaOrigen):
    if listaOrigen not in listDestino:
        os.mkdir(f"{ruteDestiny}/{listaOrigen}")
    else:
        pass


def compress(file, x):
    name, extension = os.path.splitext(file)
    if extension in ['.webp']:
        img = Image.open(f'{ruteOrigin}/{x}/{file}')
        img.save(f'{ruteDestiny}/{x}/{file}', optimize=True, quality=60)
    img = Image.open(f'{ruteOrigin}/{x}/{file}')
    img.save(f'{ruteDestiny}/{x}/{name}.webp',
             optimize=True, quality=60)


if __name__ == '__main__':
    pool1 = multiprocessing.Pool()
    pool1.map(createNewDestiny, listOrigin)
    pool2 = multiprocessing.Pool()
    for x in listOrigin:
        file = os.listdir(f"{ruteOrigin}/{x}")
        pool2.map(partial(compress, x=x), file)
