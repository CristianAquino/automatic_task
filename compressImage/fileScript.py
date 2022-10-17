import multiprocessing
from functools import partial
from PIL import Image
import os


def inputFileRoute():
    fileOrigen = input('Ingrese la ruta origen: ')
    fileDestino = input('Ingrese la ruta destino: ')
    return fileOrigen, fileDestino


def listFiles(route):
    files = os.listdir(route)
    if 'desktop.ini' in files:
        files.remove('desktop.ini')
        return files
    else:
        return files


def initThread(origen, destino, lista):
    pool = multiprocessing.Pool()
    pool.map(partial(compress, routes=(origen, destino)), lista)


def compress(file, routes):
    origen = routes[0].replace("\\", "/")
    destino = routes[1].replace("\\", "/")
    name, extension = os.path.splitext(f'{file}')
    img = Image.open(f'{origen}/{file}')
    img.save(f'{destino}/{name}.webp',
             optimize=True, quality=60)


def run():
    origen, destino = inputFileRoute()
    lista = listFiles(origen)
    initThread(origen, destino, lista)
