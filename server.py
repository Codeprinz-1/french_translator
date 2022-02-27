from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask('Web Translator')

@app.route('/englishToFrench')
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')

    return 'Translated text to French'

@app.route('/frenchToEnglish')
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')

    return 'Translated text to English'


@app.route('/')
def renderIndexPage():
    pass

if __name__ == '__main__':
    app.run(port=8000)