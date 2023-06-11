import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title('Dev Prakash')
    about_content = """
    I am Dev Prakash, a highly skilled and experienced Python and Android developer proficient in Kotlin. I hold a B.E. degree in Electronics and Communication Engineering from Sir M Visvesvarya Institute of Technology, Bangalore. Throughout my career, I have honed my skills to provide the best possible solutions to development problems. With expertise in Python and Kotlin, I am committed to delivering innovative and efficient solutions for clients' needs.
    """

    st.info(about_content)

Content2 = """
Below you can find some of apps i have built as python developer or a android Developer and many are still in Development
"""

st.write(Content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/"+row['image'])
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f'[Source Code]({row["url"]})')