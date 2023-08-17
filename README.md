db.py:
```python
import sqlite3

class DB:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.do("""
CREATE TABLE IF NOT EXISTS data (
    id INTEGER PRIMARY KEY UNIQUE NOT NULL,
    title TEXT NOT NULL,
    url TEXT NOT NULL,
    src TEXT NOT NULL,
    platform TEXT NOT NULL,
    date DATETIME DEFAULT CURRENT_TIMESTAMP
    );""")

    def insert(self, title, url, src, platform):
        self.do("INSERT INTO data (title, url, src, platform) VALUES (?, ?, ?, ?)", (title, url, src, platform))

    def do(self, sql, values=()) -> None:
        self.cursor.execute(sql, values)
        self.connect.commit()

    def read(self, sql, values=()) -> tuple:
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()

```
main.py:
```python
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

```
