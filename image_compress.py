from PIL import Image
import os
from settings import get

ruteOrigin = get('origin')
ruteDestiny = get('destino')
listOrigin = os.listdir(ruteOrigin)
listDestino = os.listdir(ruteDestiny)


def createNewDestiny():
    for x in listOrigin:
        if x not in listDestino:
            os.mkdir(f"{ruteDestiny}/{x}")
        else:
            continue


def compress():
    createNewDestiny()
    for x in listOrigin:
        for y in os.listdir(f"{ruteOrigin}/{x}"):
            name, extension = os.path.splitext(y)
            if extension in ['.webp']:
                img = Image.open(f'{ruteOrigin}/{x}/{y}')
                img.save(f'{ruteDestiny}/{x}/{y}',
                         optimize=True, quality=60)
            img = Image.open(f'{ruteOrigin}/{x}/{y}')
            img.save(f'{ruteDestiny}/{x}/{name}.webp',
                     optimize=True, quality=60)


if __name__ == '__main__':
    compress()
