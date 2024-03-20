
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Load the Jupyter Notebook file
notebook_file = 'Main_RFM_3.ipynb'
with open(notebook_file) as f:
    nb = nbformat.read(f, as_version=4)

# Execute the notebook
ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
ep.preprocess(nb, {'metadata': {'path': ''}})

# Save the executed notebook as a Python script
output_file = 'executed_notebook.py'
with open(output_file, 'w') as f:
    f.write(nbformat.writes(nb))
