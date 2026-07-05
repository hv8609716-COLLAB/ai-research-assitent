from flask import Flask, request
import os
from pdf_reader import read_pdf
from qa_engine import answer_question

app = Flask(__name__)
document_text = ""

@app.route("/", methods=["GET", "POST"])
def home():
    global document_text
    response = ""
    if request.method == "POST":
        if "pdf" in request.files:
            file = request.files["pdf"]
            if file.filename != "":
                os.makedirs("uploads", exist_ok=True)
                path = os.path.join("uploads", file.filename)
                file.save(path)
                document_text = read_pdf(path)
        question = request.form.get("question", "")
        if question:
            if document_text:
                response = answer_question(
                    question, document_text)
            else:
                response = "Pehle PDF upload karo"
    return (
        "<h1>AI Research Assistant</h1>"
        "<h3>by Harsh Vardhan</h3>"
        "<form method='POST' "
        "enctype='multipart/form-data'>"
        "<input type='file' name='pdf'><br><br>"
        "<input type='text' name='question' "
        "placeholder='Question...' size='40'>"
        "<br><br>"
        "<input type='submit' value='Submit'>"
        "</form>"
        f"<p>{response}</p>"
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=10000)
