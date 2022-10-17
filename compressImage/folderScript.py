import multiprocessing
from functools import partial
from PIL import Image
import os


def inputFolderRoute():
    folderOrigen = input('Ingrese la ruta origen: ')
    folderDestino = input('Ingrese la ruta destino: ')
    return folderOrigen, folderDestino


def listFolders(route):
    folders = os.listdir(route)
    if 'desktop.ini' in folders:
        folders.remove('desktop.ini')
        return folders
    else:
        return folders


def createFolders(origen, destino):
    foldersDestino = listFolders(destino)
    foldersOrigen = listFolders(origen)
    for folder in foldersOrigen:
        if folder not in foldersDestino:
            os.mkdir(f"{destino}/{folder}")
        else:
            pass


def initThread(origen, destino):
    listOrigen = listFolders(origen)
    pool = multiprocessing.Pool()
    for folder in listOrigen:
        file = listFolders(f'{origen}/{folder}')
        pool.map(partial(compress, routes=(origen, destino, folder)), file)


def compress(file, routes):
    origen = routes[0].replace("\\", "/")
    destino = routes[1].replace("\\", "/")
    name, extension = os.path.splitext(f'{file}')
    img = Image.open(f'{origen}/{routes[2]}/{file}')
    img.save(f'{destino}/{routes[2]}/{name}.webp',
             optimize=True, quality=60)


def run():
    origen, destino = inputFolderRoute()
    createFolders(origen, destino)
    initThread(origen, destino)
