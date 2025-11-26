import streamlit as st
import requests
import pandas as pd

st.title("Project Manager")
st.header("Add a developer")
dev_name=st.text_input("Enter Developer Name")
dev_experience=st.number_input("Enter Developer Experience (years)",min_value=0,max_value=50,value=0)
if st.button("Add Developer"):
    dev_data={"name":dev_name,"experience":dev_experience}
    response=requests.post("http://127.0.0.1:8000/developers/",json=dev_data)
    st.json(response.json())
st.header("Create Project")
p_title=st.text_input("Enter Project Title")
p_description=st.text_area("Enter Project Description")
p_lang=st.text_input("Enter Project Language")
lead_dev_name=st.text_input("Enter Lead Developer Name")
lead_dev_experience=st.number_input("Enter Lead Developer Experience",min_value=0,max_value=50,value=0)
if st.button("Create Project"):
    lead_dev_data={"name":lead_dev_name,"experience":lead_dev_experience}
    p_data={"title": p_title, "description": p_description, "languages": p_lang.split(","), "lead_developer":lead_dev_data}
    response=requests.post("http://127.0.0.1:8000/projects/",json=p_data)
    st.json(response.json())
st.header("Project Dashboard")
if st.button("Get Projects"):
    response=requests.get("http://127.0.0.1:8000/projects/")
    project_data=response.json()["projects"]
    if project_data:
        projects_df=pd.DataFrame(project_data)
        st.subheader("Projects Overview")
        st.dataframe(projects_df)
        st.subheader("Project Details")
        for project in project_data:
            st.markdown(f"### {project['title']}")
            st.markdown(f"**Description:**{project['description']}")
            st.markdown(f"**Languages Used:**{project['languages']}")
            st.markdown(f"**Lead Developer:**{project['lead_developer']['name']} with {project['lead_developer']['experience']} years of experience")
    else:
        st.warning("Project Not Found")