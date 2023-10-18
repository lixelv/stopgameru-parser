import sqlite3
from prettytable import from_db_cursor

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

    def rd(self):
        self.cursor.execute('SELECT * FROM data WHERE platform = "PC" LIMIT 2000')
        return from_db_cursor(self.cursor)

    def do(self, sql, values=None) -> None:
        if values is None:
            values = ()
        self.cursor.execute(sql, values)
        self.connect.commit()

    def read(self, sql, values=()) -> tuple:
        self.cursor.execute(sql, values)
        return self.cursor.fetchall()
