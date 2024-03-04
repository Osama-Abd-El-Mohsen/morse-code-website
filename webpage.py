from flask import Flask, render_template, request,jsonify
from morice import *
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("webpage.html", title="osama")

@app.route('/', methods=["POST"])
def operation_func():
    text = request.form.get('textbox')
    operation = request.form.get('operation')
    
    print("="*40)
    print(f"text = {text} , operation = {operation}")
    print("="*40)

    result = ""
    if operation == "add":
        result = encryptor(text)
    elif operation == "subtract":
        result = decryptor(text)

    return jsonify(result=result)


if __name__ == "__main__":
    app.run(debug=False)
