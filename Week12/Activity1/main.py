from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_flask():
    return "<p>Hello, Flash!</p> <a href='/bye'>Bye</a><a href='/learn/Elon'>learn</a>"

@app.route("/bye")
def bye():
    return "<p>Bye, Flash!</p>"

@app.route("/learn/<name>")
def learn(name):
    return f"{name} is learning Flask!"

if __name__ == "__main__":
    app.run(debug=True)