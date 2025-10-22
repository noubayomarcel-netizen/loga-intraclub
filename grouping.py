import pandas as pd

def group_by_weight(tolerance=2):
    df = pd.read_excel("athletes.xlsx")
    df = df.sort_values("Weight")
    groups = []
    while not df.empty:
        base = df.iloc[0]["Weight"]
        group = df[(df["Weight"] >= base - tolerance) & (df["Weight"] <= base + tolerance)]
        groups.append(group)
        df = df.drop(group.index)
    return groups
