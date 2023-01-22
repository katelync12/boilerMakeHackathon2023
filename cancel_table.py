import sqlite3
db_file = 'cancel.db'
conn = None
e = "Couldn't connect to db."
try:
    conn = sqlite3.connect(db_file)
    print(sqlite3.version)
except:
    print(e)

print(conn)
cur = conn.cursor()

# cur.execute("CREATE TABLE tweets(id, text)")
# cur.execute("ALTER TABLE tweets DROP COLUMN edit_history_tweet_ids")
res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchone())
# cur.execute("""
#     INSERT INTO tweets VALUES
#     ('1616825171343458304', 'RT @Spd_content: What do you think https://t.co/PfDpMlu6TD')
#     """)
tweets = dict()
tweets['0'] = "text 1"
tweets['1'] = "text 2"


for tweet in tweets:
    cur.execute("""
    INSERT INTO tweets VALUES
        (?, ?)
""", [tweet, tweets[tweet]])
    
conn.commit()
res = cur.execute("SELECT id FROM tweets")
print(res.fetchall())

# print(res.fetchone())