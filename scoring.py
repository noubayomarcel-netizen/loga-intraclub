from fpdf import FPDF
import pandas as pd

def match_sheets(brackets):
    sheets = []
    for group in brackets:
        for a, b in group:
            sheets.append({
                "A": a, "B": b,
                "score_A": 0, "score_B": 0,
                "actions_A": [], "actions_B": [],
                "winner": "Draw"
            })
    return sheets

def update_score(match, athlete, action):
    points = {
        "takedown": 2,
        "guard_pass": 3,
        "sweep": 2,
        "submission": 5
    }
    score_key = "score_A" if athlete == "A" else "score_B"
    action_key = "actions_A" if athlete == "A" else "actions_B"
    match[score_key] += points[action]
    match[action_key].append(action)
    if match["score_A"] > match["score_B"]:
        match["winner"] = "A"
    elif match["score_B"] > match["score_A"]:
        match["winner"] = "B"
    else:
        match["winner"] = "Draw"

def export_results(sheets):
    df = pd.DataFrame(sheets)
    df.to_excel("results.xlsx", index=False)
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for match in sheets:
        pdf.cell(200, 10, txt=f"{match['A']} vs {match['B']} - Winner: {match['winner']}", ln=True)
    pdf.output("results.pdf")

