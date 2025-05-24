# 🌍 Flask Language Translator API

A simple Flask-based translation API using `googletrans` library. It auto-detects the source language and translates the given text to the desired target language.

## 🚀 Live Demo

Deployed, you can access it like:

```
https://language-translate-7evj.onrender.com/translatelanguage?text=hello&target=hi
```

## 📦 Requirements

* Python 3.7+
* Flask
* googletrans (4.0.0rc1)
* gunicorn (for deployment)

## 📁 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/translator-api.git
cd translator-api
```

2. **Create virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

## ▶️ Running Locally

```bash
python app.py
```

Visit: `http://127.0.0.1:5000/translatelanguage?text=hello&target=hi`

## 📡 API Endpoint

### `/translatelanguage`

| Query Parameter | Description                   | Required |
| --------------- | ----------------------------- | -------- |
| `text`          | The text to be translated     | ✅        |
| `target`        | Language code to translate to | ✅        |

📌 **Example:**

```
https://language-translate-7evj.onrender.com/translatelanguage?text=hello&target=hi
```

📤 **Response:**

```json
{
  "text": "¿Cómo estás?"
}

```

✅ Auto detects source language
✅ Fast & simple to use
✅ JSON response

## 📜 Supported Languages

The `target` value should be a valid [Google Translate language code](https://cloud.google.com/translate/docs/languages) like:

* `en` (English)
* `hi` (Hindi)
* `fr` (French)
* `es` (Spanish)
* ...and many more.

## 🚀 Deploying on Render

1. Push your code to GitHub
2. Create a new Web Service on [Render](https://render.com/)
3. Add `gunicorn` to your `requirements.txt`
4. Set the start command as:

```bash
gunicorn app:app
```

You're live 🎉

---

## 📄 License

MIT License
