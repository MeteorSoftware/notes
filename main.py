from flask import Flask,jsonify,make_response,request

app = Flask(__name__)

class Document:
    count = 0
    def __init__(self, content=""):
        self.id = Document.count
        self.content = content
        self.addCount()
        
    def change(self, new_content):
        self.content = new_content
    
    @staticmethod
    def addCount():
        Document.count += 1
    
documents = [Document("hi"),Document("hi"),Document("hi"),Document("hi"),Document("hi"),Document("hi"),Document("hi")]




@app.route("/document/new")
def document_new():
    doc = Document("This one is new")
    documents.append(doc)
    response_data = {"id":str(doc.id), "status":"SUCCESS_DOCUMENT_CREATED"}
    return make_response(jsonify(response_data), 200)

@app.route("/document/read/<int:id>")
def document_read_id(id):
    if id > (len(documents)-1):
        response_data = {"status":"ERROR_ID_OUT_OF_BOUNDS"}
        return make_response(jsonify(response_data), 400)
    
    for document in documents:
        if document.id == id:
            response_data = {"content":str(document.content), "status":"SUCCESS_CONTENT_ACCESSED"}
            return make_response(jsonify(response_data), 200)

    response_data = {"status":"ERROR_DOCUMENT_NOT_FOUND_BY_ID"}
    return make_response(jsonify(response_data), 400)

@app.route("/document/write/<int:id>", methods=["GET", "POST"])
def document_write_id(id):
    if request.is_json:
        data = request.json
        try:
            content = data.get("content")
        except:
            response_data = {"status":"ERROR_CONTENT_MISSING_JSON"}
            return make_response(jsonify(response_data), 400)
        if id > (len(documents)-1):
            response_data = {"status":"ERROR_ID_OUT_OF_BOUNDS"}
            return make_response(jsonify(response_data), 400)
        
        for document in documents:
            if document.id == id:
                document.content = str(content)
                response_data = {"status":"SUCCESS_CONTENT_MODIFIED"}
                return make_response(jsonify(response_data), 200)

        response_data = {"status":"ERROR_DOCUMENT_NOT_FOUND_BY_ID"}
        return make_response(jsonify(response_data), 400)
    else:
        response_data = {"status":"ERROR_JSON_DATA_MISSING"}
        return make_response(jsonify(response_data), 400)

app.run(port=80, debug=True)

