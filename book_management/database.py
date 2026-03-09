import sqlite3

def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_database():
    conn = sqlite3.connect('books.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author_id INTEGER,
        book_link TEXT,
        genres TEXT,
        average_rating REAL,
        published_year INTEGER,
        FOREIGN KEY (author_id) REFERENCES authors(id))''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT)''')
    conn.commit()
    return conn, cursor
def insert_authors(cursor, authors):
    author_ids={}
    for author in authors:
        cursor.execute('''INSERT INTO authors(name) VALUES (?)''', (author,))
        cursor.execute('SELECT id FROM authors WHERE name=?', (author,))
        author_ids = cursor.fetchone()[0]
    return author_ids
def insert_books(cursor, books_dict, author_ids):
    for (title, author), info in books_dict.items():
        cursor.execute('''
            INSERT INTO books (title, author_id, book_link, genres, average_rating, published_year) VALUES (?, ?, ?, ?, ?, ?)
        ''', (title, author_ids, info['link'], ', '.join(info['genres']), float(info['average_rating'].split()[0]) if info['avg_rating'] else None, int(info['published_year'].split()[0]) if info['published_year'] else None))
def insert_data(books_dict, authors):
    conn, cursor = create_database()
    authors_ids=insert_authors(cursor, authors)
    insert_books(cursor, books_dict, authors_ids)
    conn.commit()
    conn.close()
if __name__ == '__main__':
    from books_scraper import scrape_books
    books_dict, authors = scrape_books()
    insert_data(books_dict, authors)