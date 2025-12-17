from typing import List, Optional
from pydantic import BaseModel

class RecipeBase(BaseModel):
    name: str
    description: Optional[str]
    ingredients: List[str]
    instructions: str
    cuisine: str
    difficulty: str
    category_id: int
class RecipeCreate(RecipeBase):
    pass

class Recipe(RecipeBase):
    id: int