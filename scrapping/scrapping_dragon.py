import requests
from bs4 import BeautifulSoup
import multiprocessing
from functools import partial
import shutil


def principal_process(url, manga_name, folder):
    soup = get_content(url)
    links = get_list_chapters(soup)
    initThread(links, manga_name, folder)


def get_content(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')
        return soup

    return None


def get_list_chapters(base):
    data = []
    container = base.find('ul', class_='main version-chap no-volumn')
    links = container.find_all('a')
    for info in links:
        link = info['href']
        data.append(link)
    return data


def get_img(name, link, num, folder):
    with open(f'{name} ({num}).jpg', 'wb') as file:
        file.write(requests.get(link).content)
    shutil.move(f'{name} ({num}).jpg', folder)


def set_name(ch, name):
    name = name.replace(' ', '_')
    if int(ch) < 10:
        name = f'{name}_00{ch}'
    elif int(ch) < 100:
        name = f'{name}_0{ch}'
    else:
        name = f'{name}_{ch}'
    return name


def initThread(links, manga_name, folder):
    pool = multiprocessing.Pool()
    pool.map(partial(open_link, data=(manga_name, folder)), links)


def open_link(link, data):
    conter = 1
    ch = link.split('-')[-1].split('.')[0]
    soup = get_content(link)
    container = soup.find('div', {'id': 'chapter_imgs'})
    linksimg = container.find_all('img')
    manga_name = set_name(ch, data[0])
    for img in linksimg:
        get_img(manga_name, img.get('src'), conter, data[1])
        conter += 1


if __name__ == '__main__':
    print('Bienvenido al programa de descarga de imagenes de manga')
    URL = input('Ingrese la url del manga: ')
    MANGA_NAME = input('Ingrese el nombre del manga: ')
    FOLDER = input(
        'Ingrese el nombre de la carpeta donde se guardaran las imagenes: ')
    principal_process(URL, MANGA_NAME, FOLDER)
