from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route("/"):
    return "visit url"

@app.route("/translatelanguage")
def translate_language():
    text = request.args.get("text")
    target = request.args.get("target")

    if not text or not target:
        return "Missing 'text' or 'target' parameter", 400

    translator = Translator()
    translated = translator.translate(text, dest=target)
    result = {"text": translated.text}
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
