def check_login(username, password):
    return username == "admin" and password == "loga2025"

def get_dashboard_data():
    import pandas as pd
    try:
        df = pd.read_excel("athletes.xlsx")
        return {
            "total": len(df),
            "bjj": len(df[df["sport"] == "BJJ"]),
            "wrestling": len(df[df["sport"] == "Wrestling"])
        }
    except:
        return {"total": 0, "bjj": 0, "wrestling": 0}
