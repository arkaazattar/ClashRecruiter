import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import apiKey
from clashrecruit import *
from flask import session
from dotenv import load_dotenv


load_dotenv()

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))
app = Flask(__name__, template_folder=template_dir)
app.secret_key = os.getenv("FLASK_SECRET_KEY")
CORS(app) 

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/verify-user", methods=['POST'])

def verify_user():

    data = request.get_json()

    received_tag = data.get('playerTag')
    session["player_tag"] = received_tag
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
        "receivedPlayerTag": reason,
        "recruit_status" : recruiting(received_tag)
    })

@app.route("/dashboard")
def dashboard():
        



        return render_template("dashboard.html", recruit_status = recruiting(session.get("player_tag")))
        



if __name__ == "__main__":
    app.run(debug=True, port=5000)