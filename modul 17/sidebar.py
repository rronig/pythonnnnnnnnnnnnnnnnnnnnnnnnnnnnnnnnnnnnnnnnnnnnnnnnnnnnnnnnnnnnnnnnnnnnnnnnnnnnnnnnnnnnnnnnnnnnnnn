import streamlit as st

st.sidebar.header("**Sidebar**")
st.sidebar.write("a")
st.sidebar.selectbox("Choose", [1, 2, 3])
st.sidebar.radio("Go to", [1, 2, 3])