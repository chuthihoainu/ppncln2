import streamlit as st
from markdown import markdown
st.image("download.jpg")


# Định dạng văn bản

text = "VPANDAS xin chào ngày cuối deadline"

# Hiển thị văn bản
st.write(f"""<p style="color:green;font-weight:bold;">{text}</p>""", unsafe_allow_html=True)
