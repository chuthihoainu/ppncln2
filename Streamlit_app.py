import streamlit as st
from markdown import markdown
st.image("download.jpg")
st.write("VPANDAS xin chào ạ")
text = "VPANDAS xin chào ngày cuối deadline"

# Hiển thị văn bản

markdown(f"""<p style="color:green;font-weight:bold;">{text}</p>""")
