import pandas as pd
import os

def register_athlete(name, age, weight, belt, medical, waiver, emergency):
    file = "athletes.xlsx"
    if os.path.exists(file):
        df = pd.read_excel(file)
    else:
        df = pd.DataFrame(columns=["Name", "Age", "Weight", "Belt", "Medical", "Waiver", "Emergency Contact"])
    df.loc[len(df)] = [name, age, weight, belt, medical, waiver, emergency]
    df.to_excel(file, index=False)
