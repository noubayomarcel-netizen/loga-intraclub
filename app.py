from flask import Flask, render_template, request, redirect, session, send_file
from register import save_athlete
from grouping import generate_brackets
from scoring import match_sheets, update_score, export_results
from admin import check_login, get_dashboard_data
import os

app = Flask(__name__)
app.secret_key = "securekey123"
brackets = []
sheets = []

@app.route("/")
def landing():
    return render_template("landing.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if check_login(request.form["username"], request.form["password"]):
            session["admin"] = True
            return redirect("/dashboard")
    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect("/login")
    data = get_dashboard_data()
    return render_template("dashboard.html", data=data)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        save_athlete(request.form.to_dict())
        global brackets, sheets
        brackets = generate_brackets()
        sheets = match_sheets(brackets)
        return redirect("/brackets")
    return render_template("form.html")

@app.route("/brackets")
def show_brackets():
    return render_template("brackets.html", brackets=brackets)

@app.route("/score", methods=["GET", "POST"])
def score():
    if request.method == "POST":
        match_id = int(request.form["match_id"])
        athlete = request.form["athlete"]
        action = request.form["action"]
        update_score(sheets[match_id], athlete, action)
    return render_template("score.html", sheets=sheets)
if request.method == "POST":
    match_id = int(request.form["match_id"])
    if "medal" in request.form:
        sheets[match_id]["medal"] = request.form["medal"]
    else:
        athlete = request.form["athlete"]
        action = request.form["action"]
        update_score(sheets[match_id], athlete, action)

@app.route("/export")
def export():
    export_results(sheets)
    return send_file("results.pdf", as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    @app.route("/charts")
def charts():
    return render_template("charts.html")
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")
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

