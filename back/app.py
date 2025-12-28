from flask import Flask, request, jsonify
from clashrecruit import API, Recruiter
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/verify-user', methods=['POST'])
def verify_user():
    # to do