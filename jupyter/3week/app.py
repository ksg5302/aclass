from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/user")
def show_user():
    return "O.G"

if __name__ == "__main__":
    app.run(debug=True,port=5000)
