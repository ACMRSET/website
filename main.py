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
    return render_template("events.html")


@app.route("/team")
def team_route() :

    # Ordered
    image_list = [
        {"name":"Nikhil Stephen","position":"Chair","path":"static/assets/team-members/nikhil-stephen.jpg","branch":"S6 CS"},
        {"name":"Rachel Jacob","position":"Vice Chair","path":"static/assets/team-members/rachel-jacob.jpg","branch":"S6 CS"},
        {"name":"Gautham C Sudheer","position":"Secretary","path":"static/assets/team-members/gautham-c.jpg","branch":"S6 CS"},
        {"name":"Niveditha B","position":"Joint Secretary","path":"static/assets/team-members/niveditha-b.jpg","branch":"S6 CS"},
        {"name":"Kevin Jacob","position":"Joint Secretary","path":"static/assets/team-members/kevin-benny.jpg","branch":"S6 AD"},
        {"name":"Hrithika Harish","position":"Treasurer","path":"static/assets/team-members/hritika-harish.jpg","branch":"S6 CS"},
        

    ]

    return render_template("team-page.html",image_list = image_list)
    


@app.route("/contact")
def contact_route() :
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)