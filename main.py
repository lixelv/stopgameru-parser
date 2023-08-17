import requests
from bs4 import BeautifulSoup as BS
import db

def main():
    i = 1
    d = db.DB('data.db')
    while True:
        response = requests.get(f'https://stopgame.ru/news/all/p{i}')
        soup = BS(response.content, 'html.parser')
        elements = soup.find('div', class_='list-view').find_all('div', class_='_card_1tbpr_1')
        if not elements:
            break
        for element in elements:
            image = element.find('img').get('src')
            title = element.find('a', class_='_title_1tbpr_49')
            title, url = title.get_text(), f"https://stopgame.ru{title.get('href')}"
            plat = element.find('div', class_='_tags_1tbpr_84').find('a').get_text()
            d.insert(title, url, image, plat)
        print(f'Записана {i} страница!')
        i += 1


if __name__ == '__main__':
    main()
