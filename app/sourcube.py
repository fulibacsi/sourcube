from flask import Flask, request, Response

# creating app
app = Flask(__name__)

# regustering endpoint
@app.route('/')
def main():
    return 'Welcome to SourCube!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)