import sqlite3
from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from ..models.book import Book, BookCreate, BookResponse
from ..database import  get_db_connection
from ..auth.security import get_api_key
router = APIRouter()
@router.get("/", response_model=List[Book])
def get_books():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books
@router.post("/", response_model=Book)
def create_book(book: BookCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO books (title, author_id, book_link, genres, average_rating, published_year) VALUES (?, ?, ?, ?, ?, ?)", (book.title, book.author_id, book.book_link, ",".join(book.genres) if book.genres else None, book.average_rating, book.published_year))
        conn.commit()
        book_id = cursor.lastrowid
        return Book(id=book_id, **book.dict())
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=409, detail="Book already exists")
@router.put("/{book_id}", response_model=Book)
def update_book(book_id: int, book: BookCreate, _: Depends(get_api_key())):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author_id=?, book_link=?, genres=?, average_rating=?, published_year=? WHERE id=?", (book.title, book.author_id, book.book_link, ",".join(book.genres) if book.genres else None, book.average_rating, book.published_year, book_id))
    if cursor.rowcount !=1:
        conn.close()
        raise HTTPException(status_code=404, detail="Book not found")
    conn.commit()
    conn.close()
    return Book(id=book_id, **book.dict())