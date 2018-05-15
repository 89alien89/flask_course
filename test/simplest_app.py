from flask import Flask

app = Flask(__name__)


@app.route('/')
def test():
    return "test"


app.run(port=8000, debug=True)