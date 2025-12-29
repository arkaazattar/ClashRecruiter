import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import apiKey
from clashrecruit import API

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../templates"))
app = Flask(__name__, template_folder=template_dir)
CORS(app) 


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/verify-user", methods=['POST'])


def verify_user():

    data = request.get_json()

    received_tag = data.get('playerTag')
    received_token = data.get('apiToken')
    user = API(received_tag, received_token)
    if (user.check_player_api() == True):
        status = True
        reason = "Valid User"
    else:
        status = False
        reason = f"{user.reason}"

    return jsonify({
        "message": status, 
        "receivedPlayerTag": reason
    })

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)