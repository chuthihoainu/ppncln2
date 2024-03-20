import streamlit as st
my_code='https://github.com/chuthihoainu/ppncln2/a0fac08'
with open("my_code", "r") as f:
    content = f.read()

# Hiển thị nội dung file

st.write(content)
