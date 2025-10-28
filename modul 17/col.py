import streamlit as st

col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.write("**Winter**")
    st.header("**Winter**")
with col2:
    st.write("**Spring**")
    st.header("**Spring**")