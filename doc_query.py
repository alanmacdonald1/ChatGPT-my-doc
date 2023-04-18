# Import necessary packages
from llama_index import GPTSimpleVectorIndex, Document, SimpleDirectoryReader
import os
from pathlib import Path
from llama_index import download_loader

os.environ['OPENAI_API_KEY'] = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'


DocxReader = download_loader("DocxReader")

loader = DocxReader()
documents = loader.load_data(file=Path('CV.docx'))

# Construct a simple vector index
index = GPTSimpleVectorIndex(documents)

# Querying the index
response = index.query("How can I improve this cv?")
print(response)
