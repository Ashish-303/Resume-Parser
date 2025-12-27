from flask import Flask, request, jsonify, render_template
import os

from ocr import extract_text_from_pdf
from nlp import extract_basic_info
from skills import extract_skills

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_resume():
    if "resume" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["resume"]

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(file_path)

    text = extract_text_from_pdf(file_path)
    basic_info = extract_basic_info(text)
    skills = extract_skills(text)

    return jsonify({
        "basic_info": basic_info,
        "skills": skills
    })


if __name__ == "__main__":
    app.run(debug=True)
