import streamlit as st

tab1, tab2, tab3 = st.tabs(['1', '2', '3'])

with tab1:
    st.header("Header 1")
    st.write("Tab 1")
with tab2:
    st.header("Header 2")
    st.write("Tab 2")
with tab3:
    st.header("Header 3")
    st.write("Tab 3")