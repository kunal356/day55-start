from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def bye():
    return "<p>bye</p>"

@app.route("/<name>")
def greet(name):
    return f"<p>Hello there!!! {name}</p>"

if __name__ == "__main__":
    app.run(debug=True)