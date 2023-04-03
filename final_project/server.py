from machinetranslation import translator
from machinetranslation.translator import englishToFrench, frenchToEnglish
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def translateToFrench():
    englishText = request.form['englishText']
    frenchText = englishToFrench(englishText)
    return frenchText

@app.route('/frenchToEnglish', methods=['POST'])
def translateToEnglish():
    frenchText = request.form['frenchText']
    englishText = frenchToEnglish(frenchText)
    return englishText

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
