POINTS = {
    "takedown": 2,
    "sweep": 2,
    "knee_on_belly": 2,
    "guard_pass": 3,
    "mount": 4,
    "back_control": 4
}

def add_action(sheet, athlete, action):
    if action not in POINTS:
        return
    points = POINTS[action]
    if athlete == "A":
        sheet["Actions A"].append((action, points))
        sheet["Total A"] += points
    elif athlete == "B":
        sheet["Actions B"].append((action, points))
        sheet["Total B"] += points

def decide_winner(sheet):
    if sheet["Total A"] > sheet["Total B"]:
        sheet["Winner"] = "A"
    elif sheet["Total B"] > sheet["Total A"]:
        sheet["Winner"] = "B"
    else:
        sheet["Winner"] = "Draw"
