
import os
from dotenv import load_dotenv
# this allows up to export ChatOpenAI to be used in the calling functionality
from langchain_openai import ChatOpenAI

def get_env_vars():
    load_dotenv()
    # print(os.environ["OPENAI_API_KEY"]+" is the key")



