import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
import pandas as pd
from pandas import DataFrame
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)
#load_dotenv('../../.env')
'''
DB_HOST_RPG = os.getenv("DB_HOST_RPG", default="Hey hey DB HOST pls")
DB_USER_RPG = os.getenv("DB_USER_RPG", default="Hey hey DB USER pls")
DB_NAME_RPG = os.getenv("DB_NAME_RPG", default="Hey hey DB NAME pls")
DB_PASSWORD_RPG = os.getenv("DB_PASSWORD_RPG", default="Hey hey DB PASSWORD pls")


DB_HOST_RPG = "ruby.db.elephantsql.com"
DB_USER_RPG = "ztklxebc"
DB_NAME_RPG = "ztklxebc"
DB_PASSWORD_RPG ="D1qbY3Uh3jZjSHZFjbf6lA9x8JRBfB44"


CONNECTION = psycopg2.connect(dbname=DB_NAME_RPG, user=DB_USER_RPG, password=DB_PASSWORD_RPG, host=DB_HOST_RPG)
print('CONNECTION_rpg', type(CONNECTION))

CURSOR = CONNECTION.cursor()
print('CURSOR_rpg', type(CURSOR))
'''

#Titanic Data

# titanic credentials

DB_HOST_TITANIC = "ruby.db.elephantsql.com"
DB_USER_TITANIC = "jdrqqfrz"
DB_NAME_TITANIC = "jdrqqfrz"
DB_PASSWORD_TITANIC ="SWDGLOrDEo0iO7Zd9Alk67hBh0i6oJSg"
'''

DB_HOST_TITANIC = os.getenv("DB_HOST_TITANIC", default="Hey hey DB HOST pls")
DB_USER_TITANIC = os.getenv("DB_USER_TITANIC", default="Hey hey DB USER pls")
DB_NAME_TITANIC = os.getenv("DB_NAME_TITANIC", default="Hey hey DB NAME pls")
DB_PASSWORD_TITANIC = os.getenv("DB_PASSWORD_TITANIC", default="Hey hey DB PASSWORD pls")
'''

#Connecting to a database
CONNECTION_titanic = psycopg2.connect(dbname=DB_NAME_TITANIC, user=DB_USER_TITANIC, password=DB_PASSWORD_TITANIC, host=DB_HOST_TITANIC)
print('CONNECTION_titanic', type(CONNECTION_titanic))

CURSOR_titanic = CONNECTION_titanic.cursor()
print('CURSOR_titanic', type(CURSOR_titanic))


#Read csv
DATA_PATH= os.path.join(os.path.dirname(__file__), "titanic.csv")

df = pd.read_csv(DATA_PATH)
df.index +=1
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

#using df.to_records
values=list(df.to_records(index=True))
print(type(values))

#Inserting body into titanic_table
insertion_query = f"INSERT INTO titanic_table (id, Survived, Pclass, Name,Sex, Age, SIblingSpouseAboard, ParentsChildrenAboard,Fare) VALUES %s"
execute_values(CURSOR_titanic, insertion_query,values)


CONNECTION_titanic.commit()
CURSOR_titanic.close()
CONNECTION_titanic.close()
