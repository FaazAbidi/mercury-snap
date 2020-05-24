from flask import Flask, request, jsonify
from screenshot import snap

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'mercury screenshot API'

@app.route('/snap')
def capture():

    URL = request.args.get("url")
    hosted_url = snap(URL)
    return jsonify(hosted_url)

if __name__ == '__main__':
    app.run()

