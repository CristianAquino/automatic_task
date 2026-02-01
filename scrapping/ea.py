import requests
from bs4 import BeautifulSoup

URL = 'https://www.ea.com/games/ea-sports-fc/ratings?gender=0&page=1'


def get_content(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')
        return soup

    return None


def get_species_pokemon(url):
    soup = get_content(url)

    table = soup.find_all(
        'section', class_='vitals-table')

    species = table.tbody.find_all('tr')[2].td.text

    return species


if __name__ == '__main__':
    soup = get_content(URL)

    section = soup.find_all('section')
    # rows = table.tbody.find_all('tr', limit=5)
    table = section[0].find('table')
    print(table)

    # for row in rows:
    #     # limitamos la cantidad de elementos
    #     columns = row.find_all('td', limit=3)

    #     name = columns[1].a.text
    #     type = [a.text for a in columns[2].find_all('a')]
    #     # print(*type) # mostramos la lista como un string
    #     link = DOMAIN+columns[1].a['href']

    #     species = get_species_pokemon(link)
    #     print(name, *type, species)
