import datetime

import pandas as pd
import streamlit as st
from fastapi.security import api_key
from streamlit import number_input

from book_management.routers.authors import delete_author, get_authors
import plotly as px

def dashboard_author(api_key):
    st.title("Book Management")
    st.subheader("Authors")
    authors=get_authors()
    df_authors=pd.DataFrame(authors)
    st.dataframe(df_authors,use_container_width=True)
    st.subheader("Add new author")
    new_author=st.text_input("Author name")
    if st.button("Add new author"):
        if new_author.strip():
            add_author(api_key, new_author)
        else:
            st.error("Author name cannot be blank")
    action=st.radio("Select action",["Update author","Delete author"])
    if action=="Update author":
        selected_author=st.selectbox("Select author",options=[new_author for new_author in authors])
        new_name=st.text_input("New name", value=selected_author)
        if st.button("Update author"):
            author_id=next((author['id'] for author in authors if author['name']==selected_author), None)
            update_author(api_key, author_id, new_name)
    elif action=="Delete author":
        selected_author=st.selectbox("Author", options=[new_author for new_author in authors])
        if st.button("Delete author"):
            author_id=next((author['id']for author in authors if author['name']==selected_author), None)
            delete_author(api_key, author_id)
st.subheader("Books")
books=get_books()
author=get_authors()
author_id= {author['id']: author['name'] for author in author}
for book in books:
    book['author']
    book['author_name']=author_id.get(book['author'], 'Unknown author')
    book['genres']=', '.join(book['genres'])
    del book['author_id']
df_books=pd.DataFrame(books)
st.dataframe(df_books,use_container_width=True)
st.subheader("Add book")
new_book=st.text_input("Book name")
selected_author=st.selectbox('Select author',options=[authr['name'] for authr in author], key='author_id')
new_book_average=st.number_input('Average rating',min_value=0,max_value=5, step=0.1)
new_book_genres=st.text_input('Genres')
new_book_year=st.number_input('Year',min_value=-2000000, max_value=datetime.datetime.now().year, step=1)
if st.button("Add new book"):
    if new_book.strip() and new_book_genres.strip():
        genres_list=[g.strip() for g in new_book_genres.split(',') if g.strip()]
        selected_author_id=next((authr['id'] for authr in author if authr['name']==selected_author), None)
        book_data={"title": new_book, "author_id": selected_author_id, "book_link":"", "average_rating":new_book_average, "genres": genres_list, "year": new_book_year}
        add_book(api_key, book_data)
    else:
        st.error("Book name and genres cannot be blank")
action=st.radio("Select action",["Update book","Delete book"],key='book_action')
if action=="Update book":
    selected_book=st.selectbox("Book", options=[book['title'] for book in books], key='selected_book')
    if st.button("Update book"):
        book=next((book for book in books if book['title']==selected_book), None)
        new_book_title=st.text_input("New book title", value=book['title'])
        selected_author_name=st.selectbox("Author", options=[author['name'] for author in author],index=[author['name'] for author in author], key='author_id')
        new_book_average=st.number_input('Average rating',min_value=0,max_value=5, step=0.1, value=book['average_rating'])
        new_book_genres=st.text_input('Genres', value=book['genres'])
        new_book_year=st.number_input('Year',min_value=-2000000, max_value=datetime.datetime.now().year, step=1, value=book['publication_year'])
        book_id=book['id']
        if st.button("Update book"):
            genres_list=[g.strip() for g in new_book_genres.split(',') if g.strip()]
            book_data={
                "title": new_book_title,
                "author_id": next((author['id'] for author in author if author['name']==selected_author), None),
                "book_link": book.get('book_link', ''),
                "genres": genres_list,
                "average_rating": new_book_average,
                "year": new_book_year
            }
            update_book(api_key, book_id, book_data)
elif action=="Delete book":
    bookt=st.selectbox("Book", options=[book['title'] for book in books])
    if st.button("Delete book"):
        book_id=next((book['id'] for book in books if book['title']==bookt), None)
        delete_book(api_key, book_id)
def visualization_dashboard():
    st.title("Visualization Dashboard")
    book=get_books()
    authors=get_authors()
    df_books=pd.DataFrame(books)
    if 'author_id' in df_books.columns:
        author_id={author['id']: author['name'] for author in authors}
        df_books['author']=df_books['author_id'].map(author_id)
        df_books.drop('author_id', axis=1, inplace=True)
    st.sidebar.title("Filters")
    selected_author=st.sidebar.selectbox("Author", options=["All"]+list(author_id.values()))
    min_year=int(df_books['year'].min())
    max_year=int(df_books['year'].max())
    selected_year=st.sidebar.slider("Select year", min_value=min_year, max_value=max_year, step=1, value=(min_year, max_year))
    selected_rating=st.sidebar.slider("Select rating", min_value=0, max_value=5, step=.1)
    filters=selected_author!="All" or selected_year!=(min_year, max_year)
    if st.sidebar.button("Filter") or not filters:
        filtered_books=df_books.copy()
        if filters:
            if selected_author!="All":
                filtered_books=filtered_books[filtered_books['author']==selected_author]
                filtered_books=filtered_books[(filtered_books['year']>=selected_year[0]) & (filtered_books['year']<=selected_year[1])]
                filtered_books=filters[(filtered_books['average_rating']>=selected_rating[0]) & (filtered_books['average_rating']<=selected_rating[1])]
        if not filters:
            st.subheader("Books by Year")
            books_by_year=filtered_books.groupby('year').size().reset_index(name='Count')
            fig_years=px.bar(books_by_year, x='year', y='Count', title='Books by Year', labels={"year": "Published Year", "Count": "Number of Books"},text='Count')
            fig_years.update_traces(texttemplate='%{text:.2s}', textposition='outside')
            fig_years.update_layout(informtext_minsize=8, uniformtext_mode='hide', xaxis=dict(tickmode='linear', tick0=min_year, dtick=5, tickangel=-45, tickfront=dict(size=10)), yaxis=dict(title="Number of Books", range(0, books_by_year['Count'].max()+1)), tile_x=0.5)
            st.plotly_chart(fig_>?L:"years)