from typing import List, Optional
import sqlite3
from .models import Item
from .database import get_db_connection

def create_item(item: Item) -> Item:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", (item.name, item.description))
    conn.commit()
    item.id = cursor.lastrowid
    conn.close()
    return item
def get_items() -> List[Item]:
    conn = get_db_connection()
    items=conn.execute("SELECT * FROM items").fetchall()
    conn.close()
    return [Item(**dict(item)) for item in items]

def get_item(id: int) -> Optional[Item]:
    conn = get_db_connection()
    item=conn.execute("SELECT * FROM items WHERE id=?", (id,)).fetchone()
    conn.close()
    if item is None:
        return None
    return Item(**dict(item))
def update_item(id: int, item: Item) -> Optional[Item]:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE items SET name=?, description=? WHERE id=?", (item.name, item.description, id))
    conn.commit()
    updated=cursor.rowcount()
    conn.close()
    if updated == 0:
        return None
    item.id=id
    return item
def delete_item(id: int) -> bool:
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM items WHERE id=?", (id,))
    conn.commit()
    deleted=cursor.rowcount()
    conn.close()
    return deleted>0