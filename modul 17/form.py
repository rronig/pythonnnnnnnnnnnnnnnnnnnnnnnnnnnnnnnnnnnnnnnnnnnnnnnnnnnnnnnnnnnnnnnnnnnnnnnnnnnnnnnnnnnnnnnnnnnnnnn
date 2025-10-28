import streamlit as st
with st.form('form', clear_on_submit=True):
    name=st.text_input("Enter your name")
    age=st.number_input("Enter your age", min_value=0, max_value=100)
    email=st.text_input("Enter your email")
    resume=st.text_area("Enter your resume")
    terms=st.checkbox("I agree to terms of use")
    submit=st.form_submit_button("Submit")
if submit:
    st.write(name)
    st.write(age)
    st.write(email)
    st.write(resume)
    if terms:
        st.write("Account created")