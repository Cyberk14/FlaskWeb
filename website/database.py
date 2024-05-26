import sqlite3

DB_NAME = "collected.db"

def database():
    conn = sqlite3.connect()
    conn = conn.cursor()
    
    table = conn.execute("""CREATE TABLE IF NOT EXISTS collected(
        email TEXT,
        Password TEXT)""")
    
    try:
        table_insert = f"""INSERT INTO collected
        (email, pasword)
        VALUES
        ({email}, {password})"""
