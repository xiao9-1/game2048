import sqlite3

bd = sqlite3.connect("2048.sqlite")

cur = bd.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS Records(
            name text,
            score integer)
""")

def insert_res(name, score):
    cur.execute("""
                INSERT INTO  Records values(?, ?)
    """, (name,score))
    bd.commit()

def get_best():
    cur.execute("""
                SELECT name, max(score) score 
                FROM Records
                GROUP BY name
                ORDER BY score DESC
                LIMIT 3                
    """)
    return cur.fetchall()

print(get_best())
