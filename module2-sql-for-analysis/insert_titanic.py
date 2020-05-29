import psycopg2
from psycopg2.extras import execute_values
import os
from dotenv import load_dotenv
import pandas as pd
from pandas import DataFrame
import numpy as np

psycopg2.extensions.register_adapter(np.int64, psycopg2._psycopg.AsIs)
load_dotenv()

#Titanic Data

DB_HOST_TITANIC = os.getenv("DB_HOST_TITANIC", default="Hey hey DB HOST pls")
DB_USER_TITANIC = os.getenv("DB_USER_TITANIC", default="Hey hey DB USER pls")
DB_NAME_TITANIC = os.getenv("DB_NAME_TITANIC", default="Hey hey DB NAME pls")
DB_PASSWORD_TITANIC = os.getenv("DB_PASSWORD_TITANIC", default="Hey hey DB PASSWORD pls")

print(DB_HOST_TITANIC)


#Connecting to a database
CONNECTION_titanic = psycopg2.connect(dbname=DB_NAME_TITANIC, user=DB_USER_TITANIC, password=DB_PASSWORD_TITANIC, host=DB_HOST_TITANIC)
print('CONNECTION_titanic', type(CONNECTION_titanic))

CURSOR_titanic = CONNECTION_titanic.cursor()
print('CURSOR_titanic', type(CURSOR_titanic))


#Read csv
DATA_PATH= os.path.join(os.path.dirname(__file__), "titanic.csv")

df = pd.read_csv(DATA_PATH)
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

#using df.to_records
values=list(df.to_records(index=False))
print(type(values))

#Inserting body into titanic_table
insertion_query = f"INSERT INTO titanic_table (Survived, Pclass, Name,Sex, Age, SIblingSpouseAboard, ParentsChildrenAboard,Fare) VALUES %s"
execute_values(CURSOR_titanic, insertion_query,values)


CONNECTION_titanic.commit()
CURSOR_titanic.close()
CONNECTION_titanic.close()
