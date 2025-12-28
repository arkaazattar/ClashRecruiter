
# app = Flask(__name__)
# CORS(app) 
# @app.route("/verify-user", methods=['POST'])
# def verify_user():
#     data = request.get_json()
    

#     received_tag = data.get('playerTag')
#     received_token = data.get('apiToken')

    # return jsonify({
    #     "message": "Success", 
    #     "receivedPlayerTag": received_tag
    # })



# if __name__ == "__main__":
#     app.run(debug=True, port=5000)

#####
from flask import Flask, request, jsonify
from flask_cors import CORS
import apiKey
from clashrecruit import API

app = Flask(__name__)
CORS(app) 
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

if __name__ == "__main__":
    app.run(debug=True, port=5000)