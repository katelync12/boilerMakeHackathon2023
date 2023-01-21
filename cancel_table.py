import sqlite3
db_file = 'cancel.db'
conn = None
e = "Couldn't connect to db."
try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
except Error as e:
    print(e)

print(conn)
cur = conn.cursor()

curs.execute("CREATE TABLE tweets(edit_history_tweet_ids, id, text)")
res = cur.execute("SELECT name FROM sqlite_master")

cur.execute("""
    INSERT INTO tweets VALUES
        ('1616825171343458304', '1616825171343458304', 'RT @Spd_content: What do you think https://t.co/PfDpMlu6TD'),
        ("1616825171314184196", '1616825171314184196', "RT @Patricia_Ann_E: A girl died in one of my allergy groups yesterday because after a reaction at school, no staff had access to the locked\u2026")
""")
conn.commit()
res = cur.execute("SELECT text FROM tweets")
print(res.fetchall())

# print(res.fetchone())
