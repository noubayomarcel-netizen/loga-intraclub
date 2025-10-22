from flask import Flask, render_template, request
import register
import grouping
import brackets
import score_sheets
from scoring import add_action, decide_winner

app = Flask(__name__)

# These will be created after registration
groups = []
brackets_data = []
match_sheets = []

@app.route("/", methods=["GET", "POST"])
def home():
    global groups, brackets_data, match_sheets
    if request.method == "POST":
        # Save athlete info
        register.register_athlete(
            request.form["name"],
            int(request.form["age"]),
            float(request.form["weight"]),
            request.form["belt"],
            request.form["medical"],
            request.form["waiver"],
            request.form["emergency"]
        )
        # After registration, regenerate groups and brackets
        groups = grouping.group_by_weight()
        brackets_data = brackets.generate_brackets(groups)
        match_sheets = score_sheets.create_score_sheets(brackets_data)
    return render_template("form.html")

@app.route("/brackets")
def show_brackets():
    return render_template("brackets.html", brackets=brackets_data)

@app.route("/score", methods=["GET", "POST"])
def score_match():
    global match_sheets
    if request.method == "POST":
        match_id = int(request.form["match_id"])
        athlete = request.form["athlete"]
        action = request.form["action"]
        add_action(match_sheets[match_id], athlete, action)
        decide_winner(match_sheets[match_id])
    return render_template("score.html", sheets=match_sheets)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



