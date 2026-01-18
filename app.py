from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! everyone This is version 2 of my deployed app"

if __name__=="__main__":
    app.run(debug=True)