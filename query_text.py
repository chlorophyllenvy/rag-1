from langchain_community.vectorstores import LanceDB
from langchain_openai import OpenAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from helpers.setup import get_env_vars, ChatOpenAI
import json
from flask import jsonify


def query_pdf():
    get_env_vars()

    llm = ChatOpenAI(model="gpt-4o-mini")
    # LanceDB
    LANCEDB_HOST_FILE = '../data_store/langchain'
    TBL_NAME = "pdf_table"
    vectorstore = LanceDB(
        uri=LANCEDB_HOST_FILE,
        embedding=OpenAIEmbeddings(),
        table_name=TBL_NAME
        )
    retriever = vectorstore.as_retriever()


    system_prompt = (
        "You are an assistant for question-answering tasks. "
        "Use the following pieces of retrieved context to answer "
        "the question. If you don't know the answer, say that you "
        "don't know. Use three sentences maximum and keep the "
        "answer concise."
        "\n\n"
        "{context}"
    )

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system_prompt),
            ("human", "{input}"),
        ]
    )


    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)

    result = rag_chain.invoke({"input": "What happened in animal reproduction studies?"})

    # print(len(result['context']), result['context'][0])

    # print(result, result.keys(),len(result['context']), result['answer'])

    # print(json.loads('{"answer": "'+result["answer"]+'")}'))
    # print(jsonify(result['answer']))
    # result_doc = jsonify({'answer':result['answer']})


    return result
