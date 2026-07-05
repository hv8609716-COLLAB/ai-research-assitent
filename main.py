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

        # PDF upload
        if "pdf" in request.files:
            file = request.files["pdf"]

            if file.filename != "":

            
                os.makedirs("uploads", exist_ok=True)

                # file save
                path = os.path.join("uploads", file.filename)

                file.save(path)

                # pdf read
                document_text = read_pdf(path)

        
        question = request.form.get("question", "")

        if question:

            if document_text:
                response = answer_question(
                    question,
                    document_text
                )
            else:
                response = " PDF upload"
                
     return f"""
<html>
<body>
<h1>AI Research Assistant</h1>
<form method="POST" enctype="multipart/form-data">
<input type="file" name="pdf"><br><br>
<input type="text" name="question" 
placeholder="Question likho..."><br><br>
<input type="submit" value="Submit">
</form>
<p>{response}</p>
</body>
</html>
    """


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=10000)
    
    



