from flask import Flask,jsonify,make_response,request
from flask_sqlalchemy import SQLAlchemy
import utils

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost/postgres"
db = SQLAlchemy(app)



class Documents(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(255))
    body=db.Column(db.Text)
    
@app.route("/documents/get/<int:id>")
def get_documents(id):
    doc = db.get_or_404(Documents, id)
    print(doc.id)
    return utils.success(jsonify(doc.id, doc.title,doc.body))

@app.route("/documents/create")
def create_document():
    doc = Documents(title="New document", body="Hello there")
    db.session.add(doc)
    db.session.commit()
    return utils.success(jsonify(doc.id))

@app.route("/documents/write/<int:id>", methods=["POST"])
def modify_document(id):
    if request.is_json:
        data = request.get_json()
        try:
            title = data.get("title")
            body = data.get("body")
        except:
            return utils.fail400({"error":"json is missing required fields"})
        doc = db.get_or_404(Documents, id)
        doc.title = title
        doc.body = body
        db.session.commit()
        return utils.success(jsonify(doc.id))
    return utils.fail400({"error":"request is not json"})



"""

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

"""        

app.run(port=80, debug=True)

