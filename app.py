from flask import Flask, render_template, request, redirect, session
from scoring import generate_brackets, match_sheets, update_score, export_results
from admin import check_login, get_dashboard_data

app = Flask(__name__)
app.secret_key = "loga_secret_key"

athletes = []
brackets = []
sheets = []

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    global athletes, brackets, sheets
    if request.method == "POST":
        name = request.form["name"]
        weight = int(request.form["weight"])
        sport = request.form["sport"]
        athletes.append({"name": name, "weight": weight, "sport": sport})
        brackets = generate_brackets(athletes)
        sheets = match_sheets(brackets)
    return render_template("register.html", athletes=athletes)

@app.route("/delete/<name>")
def delete_athlete(name):
    global athletes
    athletes = [a for a in athletes if a["name"] != name]
    return redirect("/register")

@app.route("/clear")
def clear_athletes():
    global athletes, brackets, sheets
    athletes = []
    brackets = []
    sheets = []
    return redirect("/register")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if check_login(request.form["username"], request.form["password"]):
            session["admin"] = True
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
