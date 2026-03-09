import pandas as pd

def transform(df):

    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    df = df.rename(columns={"cast": "cast_members"})

    df = df.drop_duplicates()

    df["director"] = df["director"].fillna("Unknown")

    df["date_added"] = pd.to_datetime(df["date_added"], errors="coerce")

    return df