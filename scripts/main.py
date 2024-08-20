import requests
import os
from flask import Flask, jsonify, request
from flask_cors import CORS

from scripts.gcp_services import GoogleServices


google_services = GoogleServices()

app = Flask(__name__)
# Enable Cross Origin Scripting
CORS(app)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


"""The routes"""
@app.route("/")
@app.route("/home")
def home_route() :
    pass


@app.route("/events")
def events_route() :
    pass


@app.route("/team")
def team_route() :
    pass


@app.route("/contact", methods=["POST"])
def contact_route() :
    if request.method == "POST" :
        response = request.json
        sender = response["email"]
        body = response["message"]
        name = response["name"]
        
        subject = f"New message from {name} | {sender}"
        body += f"\n\nFor further communication, reach out to {name} at {sender}"
        receiver = os.getenv("ACMRSET_MAIL")
        
        status, issue = google_services.send_email(receiver, subject, body)
        if status :
            return jsonify({
                "Status": "Success",
                "Response": "Message successfully sent",
                "Issues": issue
            }), 200

        else :
            return jsonify({
                "Status": "Failure",
                "Response": "Message could not be sent",
                "Issues": issue
            }), 503