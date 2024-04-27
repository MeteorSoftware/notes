from flask import Flask,jsonify,make_response

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
    documents.append(Document("hi"))
    response_data = {"id":str()}
    return "a"
    


app.run(port=80, debug=True)

