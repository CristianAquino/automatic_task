import requests
from bs4 import BeautifulSoup

DOMAIN = 'https://pokemondb.net'
URL = '/pokedex/all'


def get_content(url):
    response = requests.get(url)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')
        return soup

    return None


def get_species_pokemon(url):
    soup = get_content(url)

    table = soup.find(
        'table', class_='vitals-table')

    species = table.tbody.find_all('tr')[2].td.text

    return species


if __name__ == '__main__':
    soup = get_content(DOMAIN+URL)

    table = soup.find('table', {'id': 'pokedex'})
    rows = table.tbody.find_all('tr', limit=5)

    for row in rows:
        # limitamos la cantidad de elementos
        columns = row.find_all('td', limit=3)

        name = columns[1].a.text
        type = [a.text for a in columns[2].find_all('a')]
        # print(*type) # mostramos la lista como un string
        link = DOMAIN+columns[1].a['href']

        species = get_species_pokemon(link)
        print(name, *type, species)
