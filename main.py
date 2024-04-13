from flask import Flask, redirect, render_template


app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route("/", "/home")
def home_route() :
    pass


@app.route("/events")
def events_route() :
    pass


@app.route("/team")
def events_route() :
    pass


@app.route("/contact")
def contact_route() :
    pass