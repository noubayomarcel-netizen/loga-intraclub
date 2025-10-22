import pandas as pd

def save_athlete(data):
    try:
        df = pd.read_excel("athletes.xlsx")
    except:
        df = pd.DataFrame()
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_excel("athletes.xlsx", index=False)

