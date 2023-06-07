import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Matas Šliuževičius")
    content = """ Hello, I'm currently learning python and looking for 
    entry/junior level job """
    st.info(content)

st.subheader("Below you can find some of the app I have built in Python")

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f'images/{row["image"]}')
        st.write(f'[Source code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f'[Source code]({row["url"]})')


