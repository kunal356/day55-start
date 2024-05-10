from flask import Flask
app = Flask(__name__)

def make_bold(funct):
    def wrapper_function(*args, **kwargs):
        val = f"<b>{funct(*args, **kwargs)}<b>"
        return val
    return wrapper_function

def make_italic(funct):
    def wrapper_function(*args, **kwargs):
        val = f"<em>{funct(*args, **kwargs)}<em>"
        return val
    return wrapper_function

def make_underline(funct):
    def wrapper_function(*args, **kwargs):
        val = f"<u>{funct(*args, **kwargs)}<u>"
        return val
    return wrapper_function

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye(greet="bye"):
    return f"{greet}"

@app.route("/<name>")
def greet(name):
    return f"<p>Hello there!!! {name}</p>"

if __name__ == "__main__":
    app.run(debug=True)