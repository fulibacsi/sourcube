from flask import Flask, request, Response, render_template
from model.generate import train, generate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('sourcube.html')

@app.route('/generate', methods=['POST'])
def generate_text():
    text = request.values.get('text', '')
    model, le = train(text)
    return generate(model, le, 10)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
