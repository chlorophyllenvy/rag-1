from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import DirectoryLoader

async def buildPDF(file_path):
    # loader = PyPDFLoader(file_path)
    loader = [DirectoryLoader('/path/to/cricket/files', glob="./*.pdf", loader_cls=PyPDFLoader).load()]
    pages = []
    async for page in loader.alazy_load():
        pages.append(page)

    return  pages
