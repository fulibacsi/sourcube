from flask import Flask, request, Response, render_template

# creating app
app = Flask(__name__)

# regustering endpoint
@app.route('/')
def main():
    return render_template('sourcube.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)