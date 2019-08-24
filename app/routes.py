from app import app

from flask import render_template, request
from app.model.generate import train, generate


@app.route('/')
def index():
    return render_template('sourcube.html')


@app.route('/generate', methods=['POST'])
def sourcube_me():
    text = request.values.get('text', '')
    model, le = train(text)
    return generate(model, le, 10)
