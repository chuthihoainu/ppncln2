import streamlit as st
st.title("hello")


# Mở file Python
with open("Main_RFM_#.ipynb", "r") as f:
    content = f.read()

# Hiển thị nội dung file
st.code(content, language="python")
