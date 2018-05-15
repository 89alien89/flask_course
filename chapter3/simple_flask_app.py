from flask import Flask

app = Flask(__name__)

@app.route('/')
def main():
    return  "My first flask app"


app.run(port=8000)