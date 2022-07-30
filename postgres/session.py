import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="linkedin_db",
    user="postgres",
    password="password")

curs = conn.cursor()
curs.execute("ROLLBACK")
conn.commit()

cur = conn.cursor()

# execute a statement
print('PostgreSQL database version:')
cur.execute('SELECT version()')
db_version = cur.fetchone()
print(db_version)
cur.close()