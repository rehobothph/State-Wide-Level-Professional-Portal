from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to State-Wide Level Professional Portal</h1>"

if __name__ == "__main__":
    app.run(debug=True)
