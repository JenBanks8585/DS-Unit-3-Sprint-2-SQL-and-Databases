
import psycopg2
from psycopg2.extras import DictCursor, execute_values
import os
from dotenv import load_dotenv
import json
import pandas as pd

load_dotenv('../../.env')

DB_HOST = os.getenv("DB_HOST", default="Hey hey DB HOST pls")
DB_USER = os.getenv("DB_USER", default="Hey hey DB USER pls")
DB_NAME = os.getenv("DB_NAME", default="Hey hey DB NAME pls")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="Hey hey DB PASSWORD pls")


CONNECTION = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
print('CONNECTION', type(CONNECTION))

CURSOR = CONNECTION.cursor(cursor_factory=DictCursor)
print('CURSOR', type(CURSOR))


### An example query
CURSOR.execute('SELECT * from test_table;')
### Note - nothing happened yet! We need to actually *fetch* from the cursor
results = CURSOR.fetchone()

print(type(results))
print(results)



#
# CREATE THE TABLE
#
table_name = "test_table2"

print("-------------------")
query = f"""
CREATE TABLE IF NOT EXISTS {table_name} (
  id SERIAL PRIMARY KEY,
  name varchar(40) NOT NULL,
  data JSONB
);
"""
print("SQL:", query)
CURSOR.execute(query)

#
# INSERT SOME DATA
# Method 1, insert one row or few rows at a time

my_dict = { "a": 1, "b": ["dog", "cat", 42], "c": 'true' }


insertion_query = f"INSERT INTO {table_name} (name, data) VALUES (%s, %s)"
CURSOR.execute(insertion_query,
  ('A rowwwww', 'null')
)
CURSOR.execute(insertion_query,
 ('Another row, with JSONNNNN', json.dumps(my_dict))
)


# Method 2, insert more rows at a time

# h/t: https://stackoverflow.com/questions/8134602/psycopg2-insert-multiple-rows-with-one-query

insertion_query2 = f"INSERT INTO {table_name} (name, data) VALUES %s"
execute_values(CURSOR, insertion_query2, [
  ('A rowwwww', 'null'),
  ('Another row, with JSONNNNN', json.dumps(my_dict)),
  ('Third row', "3")
])



# ACTUALLY SAVE THE TRANSACTIONS
CONNECTION.commit()

CURSOR.close()
CONNECTION.close()

