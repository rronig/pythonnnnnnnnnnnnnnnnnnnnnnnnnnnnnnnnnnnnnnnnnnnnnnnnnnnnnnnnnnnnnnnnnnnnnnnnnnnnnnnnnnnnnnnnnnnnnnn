from pydantic import BaseModel
import streamlit as st

class MovieCreate(BaseModel):
    title: str
    director: str

class Movie(MovieCreate):
    id: int