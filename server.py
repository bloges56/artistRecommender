from flask import Flask
from flask.helpers import send_from_directory
from flask_cors import CORS, cross_origin


app = Flask(__name__, static_folder='client/build')
CORS(app)

@app.route("/members")
@cross_origin()
def members():
    return {"members": ["Member1", "Member2", "Member3"]}

@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    app.run(debug=True)

