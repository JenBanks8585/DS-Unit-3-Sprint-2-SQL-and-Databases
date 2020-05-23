import psycopg2

DB_HOST ="rajje.db.elephantsql.com"
DB_USER ="leiccvgo"
DB_NAME ="leiccvgo"
DB_PASSWORD ="5chB8T1tdvA1opnTbvDbcla_wBomNUml"

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print(type(conn))
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
print(type(cur))

breakpoint()
### An example query
cur.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = cur.fetchone()

print(type(results))
print(results)