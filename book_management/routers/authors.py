from typing import List
from fastapi import APIRouter, Depends, HTTPException
from ..models.author import Author, AuthorCreate
from ..database import get_db_connection

router = APIRouter()

@router.get("/", response_model=List[Author])
def get_authors():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(f"SELECT id, name FROM authors;")
    authors = cursor.fetchall()
    conn.close()
    return [{"id": author[0], "name": author[1]} for author in authors]

@router.delete("/{id}", response_model=Author)
def delete_author(id: int, _: str = Depends(get_api_key)):
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(f"DELETE FROM authors WHERE id={id};")
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Author not found")
    conn.commit()
    conn.close()
    return {"detail": "Author deleted"}
