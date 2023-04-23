import streamlit as st


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