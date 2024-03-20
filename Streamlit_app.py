import streamlit as st
my_code=''
with open("my_code", "r") as f:
    content = f.read()

# Hiển thị nội dung file

st.write(content)
