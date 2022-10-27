from flask import Flask
import os
app = Flask(__name__)

@app.route("/")
def home():
    return "First task of Assignment 4 was done!!"

if __name__ == "__main__":
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0',port=port)