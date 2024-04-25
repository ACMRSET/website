from flask import Flask, redirect, render_template


app = Flask(__name__)
# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


"""The routes"""
@app.route("/")
@app.route("/home")
def home_route() :
    
    return render_template("home-page.html")


@app.route("/events")
def events_route() :
    pass


@app.route("/team")
def team_route() :
    return render_template("team-page.html")
    


@app.route("/contact")
def contact_route() :
    pass


if __name__ == "__main__":
    app.run(debug=True)