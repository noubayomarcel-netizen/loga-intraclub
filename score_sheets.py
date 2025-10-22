def create_score_sheets(brackets):
    sheets = []
    for i, bracket in enumerate(brackets):
        for match in bracket:
            sheets.append({
                "Group": i + 1,
                "Match": f"{match[0]} vs {match[1]}",
                "Actions A": [],
                "Actions B": [],
                "Total A": 0,
                "Total B": 0,
                "Winner": ""
            })
    return sheets
