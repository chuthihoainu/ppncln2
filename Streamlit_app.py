
import streamlit as st
import pandas as pd

# Load the Jupyter Notebook file from GitHub
url = 'https://raw.githubusercontent.com/your_username/your_repository/main/your_notebook.ipynb'

# Display the content of the Jupyter Notebook file
st.markdown(f"### Displaying Jupyter Notebook from GitHub\n[Click here to view the notebook]({url})")
streamlit run your_script.py
