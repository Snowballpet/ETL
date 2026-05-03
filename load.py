import sqlite3

def load_data(df):
    conn = sqlite3.connect("data.db")
    df.to_sql("records", conn, if_exists="replace", index=False)
    conn.close()
