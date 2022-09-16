import requests
from bs4 import BeautifulSoup
from settings import get
import os

url = get('page')

lista = []

res = requests.get(url)
soup = BeautifulSoup(res.content, 'html.parser')
img = soup.find_all('img', attrs={'class': 'wp-manga-chapter-img'})

for x in img:
    a = x['src']
    b = x['src'].split('_')[-1:]
    name, extension = os.path.splitext(b[0])
    nombre_local_imagen = f"{name}{extension}"
    imagen = requests.get(a).content
    with open(nombre_local_imagen, 'wb') as handler:
        handler.write(imagen)
# https: // parzibyte.me/blog/2018/03/26/descargar-imagen-gif-png-jpg-python/
