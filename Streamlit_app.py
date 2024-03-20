import streamlit as st
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Load the Jupyter Notebook file from GitHub
url = 'https://github.com/chuthihoainu/ppncln2/master/Main_RFM_3.ipynb'

# Read the Jupyter Notebook content
with st.spinner('Loading the notebook...'):
    nb = nbformat.reads(requests.get(url).text, as_version=4)

# Execute the notebook
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': ''}})

# Display the output cells in Streamlit
st.markdown("### Displaying Jupyter Notebook Results")
for cell in nb.cells:
    if cell.cell_type == 'code' and cell.outputs:
        st.write('```python')
        st.code(cell.source)
        st.write('```')
        for output in cell.outputs:
            if output.output_type == 'execute_result':
                st.write(output.data['text/plain'])
            elif output.output_type == 'display_data':
                st.image(output.data['image/png'])
