import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = 'https://news.google.com/topics/CAAqLQgKIidDQkFTRndvSkwyMHZNR1ptZHpWbUVnWmxjeTAwTVRrYUFsQkZLQUFQAQ?hl=es-419&gl=PE&ceid=PE%3Aes-419'

if __name__ == '__main__':
    response = requests.get(URL)

    if response.status_code == 200:
        content = response.text
        soup = BeautifulSoup(content, 'html.parser')

        news = soup.find_all('h4', class_='JtKRv', limit=20)

        print('Iniciando descarga de archivo')

        now = datetime.now().strftime('%d_%m_%Y')

        with open(f'news/news_{now}.txt', 'w+') as file:
            for new in news:
                title = new.text
                file.write(title + '\n')
        print('Archivo guardado')
