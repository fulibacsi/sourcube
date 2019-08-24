from app import app


from flask import render_template, request
from app.model.generate import train, generate


@app.route('/')
def index():
    return render_template('sourcube.html')


@app.route('/generate', methods=['POST'])
def sourcube_me():
    model = train(request.values.get('text', ''))
    return generate(model)
