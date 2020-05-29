import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
import pandas as pd
from pandas import DataFrame
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)

#load_dotenv()


#Titanic Data

# titanic credentials
DB_HOST_TITANIC_PG = "ruby.db.elephantsql.com"
DB_USER_TITANIC_PG = "dqomdcuz"
DB_NAME_TITANIC_PG = "dqomdcuz"
DB_PASSWORD_TITANIC_PG ="71YD9d1cbSko24-V57i02y9d_MEUj8oJ"
'''
DB_HOST_TITANIC_PG = os.getenv("DB_HOST_TITANIC_PG", default="Hey hey DB HOST pls")
DB_USER_TITANIC_PG = os.getenv("DB_USER_TITANIC_PG", default="Hey hey DB USER pls")
DB_NAME_TITANIC_PG = os.getenv("DB_NAME_TITANIC_PG", default="Hey hey DB NAME pls")
DB_PASSWORD_TITANIC_PG = os.getenv("DB_PASSWORD_TITANIC_PG", default="Hey hey DB PASSWORD pls")
'''
print(DB_HOST_TITANIC_PG)


#Connecting to a database
CONNECTION_titanic = psycopg2.connect(dbname=DB_NAME_TITANIC_PG, user=DB_USER_TITANIC_PG, password=DB_PASSWORD_TITANIC_PG, host=DB_HOST_TITANIC_PG)
print('CONNECTION_titanic', type(CONNECTION_titanic))

CURSOR_titanic = CONNECTION_titanic.cursor()
print('CURSOR_titanic', type(CURSOR_titanic))


#Read csv
df = pd.read_csv(r'C:\Users\J8015\Desktop\repo\unit3\DS-Unit-3-Sprint-2-SQL-and-Databases\module2-sql-for-analysis\titanic.csv')
#df.index +=1
print(type(df))

#Grabbing column names
header = df.columns.values.tolist()
print(len(header))

#Grabbing body of dataframe converted to a list
body_frame = (df.values.tolist())
print(type(body_frame))

# Creating a table query
query = f"""
CREATE TABLE IF NOT EXISTS Titanic_table (
  id SERIAL PRIMARY KEY,
  Survived INT4,
  Pclass INT4,
  Name TEXT,
  Sex TEXT, 
  Age FLOAT8, 
  SIblingSpouseAboard INT4,
  ParentsChildrenAboard INT4,
  Fare numeric
);"""


#Executing table creation query
print("SQL:", query)
CURSOR_titanic.execute(query)
print(type(CURSOR_titanic.execute(query)))

#using df.to_records
values=list(df.to_records(index=False))
print(type(values))

#Inserting body into titanic_table
insertion_query = f"INSERT INTO titanic_table (Survived, Pclass, Name,Sex, Age, SIblingSpouseAboard, ParentsChildrenAboard,Fare) VALUES %s"
execute_values(CURSOR_titanic, insertion_query,values)

#Quesries: 
queries = [
    "SELECT COUNT(survived) as surv_count FROM titanic_table WHERE survived = 1;",
    "SELECT COUNT(pclass) as class1 FROM titanic_table WHERE pclass = 1;"
    ]

for query in queries:
    print("--------------")
    print(f"QUERY: '{query}'")

    obj = CURSOR_titanic.execute(query)
    print("OBJ", type(obj))
    print(obj) #> <class 'sqlite3.Cursor'>

    results = CURSOR_titanic.execute(query).fetchone()
    print("RESULTS:", type(results))
    print(results[0])

    print(type(results[0])) #> type(results[0])
    breakpoint()


CONNECTION_titanic.commit()
CURSOR_titanic.close()
CONNECTION_titanic.close()