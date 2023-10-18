import db

def main():
    d = db.DB('data.db')
    print(d.rd())


if __name__ == '__main__':
    main()
