from fastapi import APIRouter
from typing import List
from .. import database
from ..models.category import Category

router = APIRouter()

@router.get("/", response_model=List[Category])
def read_categories():
    """Retrieves all movies from the database."""
    return database.read_categories()