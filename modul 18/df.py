import pandas as pd
import streamlit as st

st.header("Displaying dataframes")
data=pd.DataFrame({'Name': ['Alice', 'Bob'], "Age": [1, 2], "City": ["London", "Paris"]})
st.write(data)