import streamlit as st
import pandas


st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title('Dev Prakash')
    about_content = """
    Hi,I am Dev Prakash, a highly skilled and experienced Python developer as well as an Android developer proficient in Kotlin. I graduated from Sir M Visvesvarya Institute of technology,bangalore as a Bachelors of engineering(B.E) in Electronics and communication Engineering, I have honed my skills and expertise to provide the best possible solutions to any development problem.
    
    """

    st.info(about_content)

Content2 = """
Below you can find some of apps i have built as python developer or a android Developer
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