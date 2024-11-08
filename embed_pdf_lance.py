from langchain_community.vectorstores import LanceDB
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter, RecursiveCharacterTextSplitter

from helpers.loadPDF import buildPDF
import asyncio
from helpers.setup import get_env_vars, ChatOpenAI

def embed_pdf():
    get_env_vars()
    ChatOpenAI(model="gpt-4o-mini")

    file_path = ["corpus/LIVALO_PI_CURRENT.pdf", "LIVALO® Coupon _ Download Savings Card.pdf"]
    file_path2 = "LIVALO® Coupon _ Download Savings Card.pdf"
    pages =  asyncio.run(buildPDF(file_path))
    docs = pages
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)

    documents = CharacterTextSplitter().split_documents(splits)
    embeddings = OpenAIEmbeddings()
    LANCEDB_HOST_FILE = './data_store/langchain'
    TBL_NAME = "pdf_table"

    vector_store = LanceDB(
        uri=LANCEDB_HOST_FILE,
        embedding=OpenAIEmbeddings(),
        table_name=TBL_NAME
        )
    finished = vector_store.add_documents(documents)
    return finished