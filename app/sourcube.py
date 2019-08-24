from flask import Flask, request, Response, render_template
from model.generate import generate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sourcube.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    return generate(request.values.get('text', ''))

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)