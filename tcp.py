import sqlite3

db = sqlite3.connect('db.db')
sql = db.cursor()

sql.execute("""
CREATE TABLE IF NOT EXISTS myTable
(
    name TEXT,
    birth TEXT,
    subject TEXT,
    length TEXT,
    sum TEXT,
    prem TEXT,
    agent TEXT,
    KVall TEXT,
    KVget TEXT
)""")
db.commit()
db.close()
