import streamlit as st

st.set_page_config()

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=300)

with col2:
    st.title("Matas Šliuževičius")
    content = """ Hello, I'm currently learning python and looking for 
    entry/junior level job """
    st.info(content)
