from flask import Flask, request
import requests
import os
from flask import jsonify
from helpers.base_document import Document


app = Flask(__name__)



@app.route('/')
def hello_world():
    return 'Hello Troy'


@app.route('/list')
def list_all_files():
    allDirs = list(os.walk("corpus"))
    #    print(allDirs)

    return jsonify({"allDirs": allDirs})




@app.route('/test')
def testing():
    directories = []
    list = {}
    for root, dirs, files, rootfd in os.fwalk(os.getcwd()):
        for name in files:
            print("file", name)
        for name in dirs:
            if name == 'node_modules' or name == 'venv':
                continue
            # print("dir", name)
            directories.append(name)
            for files, dirs in os.fwalk(name):
                print(files)
                list[name] = files

        print(directories)
        print(list)
        return json.dumps({"music": list})




@app.route('/embed', methods=['GET'])
def embed():
   from embed_pdf_lance import embed_pdf
   res = embed_pdf()
   string_list = [str(element) for element in res]
   print(string_list)
   return 'is finished'


@app.route('/query', methods=['POST'])
def query():
   from query_text import query_pdf
   query_results = query_pdf()
   answer = query_results['answer']
   context = [{"page_content": doc.page_content, "metadata": doc.metadata} for doc in query_results['context']]

   return {'answer':answer, 'context':context}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)