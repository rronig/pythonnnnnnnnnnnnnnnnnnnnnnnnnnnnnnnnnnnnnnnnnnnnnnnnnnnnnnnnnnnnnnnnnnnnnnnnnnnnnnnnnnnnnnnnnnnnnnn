import streamlit as st
import pandas as pd
import plotly.express as px

books_df=pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling book analysis")
st.write("This app analyzes Amazon's top-selling books")

st.subheader("Summary statistics")
total_books=books_df.shape[0]
unique_titles=books_df['Name'].unique()
average_rating=books_df['User Rating'].mean()
average_price=books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric(f"Average rating", f"{average_rating:.2f}")
col2.metric(f"Average price", f"{average_price:.2f}")
col3.metric("Total books", total_books)
col4.metric("Unique titles", len(unique_titles))
st.subheader("Most popular books")
st.write(books_df.head())
col11, col12=st.columns(2)
with col11:
    st.subheader("Most popular books")
    top_tiles=books_df['Name'].value_counts().head(10)
    st.bar_chart(top_tiles)
with col12:
    st.subheader("Most popular authors")
    top_authors=books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)
fig=px.pie(books_df, names='Genre', title='Genre', color='Genre', color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)
size=books_df.groupby(['Year', 'Genre']).size().reset_index(name='counts')
fig=px.bar(size, x='Year', y='counts', title='Genre')
st.plotly_chart(fig)
top_authors=books_df['Author'].value_counts().head(10)
top_authors.columns=['Count', 'Author']

fig=px.bar(top_authors, x='count', y='Author', title='Top Authors', orientation='h', labels={'Count': 'Count', 'Author': 'Author'}, color='count', color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)