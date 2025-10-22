import pandas as pd

def generate_brackets():
    df = pd.read_excel("athletes.xlsx")
    df = df.sort_values(by="weight")
    groups = []
    used = set()

    for i, athlete in df.iterrows():
        if i in used:
            continue
        group = [athlete["name"]]
        used.add(i)
        for j, other in df.iterrows():
            if j in used or i == j:
                continue
            if abs(athlete["weight"] - other["weight"]) <= 2 and athlete["sport"] == other["sport"]:
                group.append(other["name"])
                used.add(j)
        matches = []
        for k in range(0, len(group), 2):
            a = group[k]
            b = group[k+1] if k+1 < len(group) else "BYE"
            matches.append((a, b))
        groups.append(matches)
    return groups
