def transform_data(df):
    df = df.dropna()
    df.columns = [c.lower().replace(" ", "_") for c in df.columns]
    return df
