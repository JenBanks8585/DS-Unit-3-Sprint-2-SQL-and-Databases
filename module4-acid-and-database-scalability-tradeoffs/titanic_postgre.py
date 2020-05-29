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

#Queries: 

#--1. How many passengers survived, and how many died?

query1= """
SELECT COUNT(survived) as surv_count
FROM titanic_table
WHERE survived = 1;
"""
'''
#--2. How many passengers were in each class?
SELECT COUNT(pclass) as class1
FROM titanic_table
WHERE pclass = 1;

SELECT COUNT(pclass) as class2
FROM titanic_table
WHERE pclass = 2;

SELECT COUNT(pclass) as class3
FROM titanic_table
WHERE pclass = 3;

#--3. How many passengers survived/died within each class?
SELECT count(pclass) as p1_count
FROM titanic_table
WHERE survived = 1
AND pclass = 1;

SELECT count(pclass) as p2_count
FROM titanic_table
WHERE survived = 1
AND pclass = 2;

SELECT count(pclass) as p3_count
FROM titanic_table
WHERE survived = 1
AND pclass = 3;

#--4. What was the average age of survivors vs nonsurvivors? 
#--   survivor = 28.4083918128655, died = 30.1385321100917
SELECT AVG(age) as avg_age_surv
FROM titanic_table
WHERE survived =1;

SELECT AVG(age) as avg_age_died
FROM titanic_table
WHERE survived =0;

#--5. What was the average age of each passenger class?
#-- pclas1 = 38.7889814814815, pclass2 = 29.8686413043478, pclass3 = 25.1887474332649
SELECT AVG(age) as p1_ave_age
FROM titanic_table
WHERE pclass = 1;

SELECT AVG(age) as p2_ave_age
FROM titanic_table
WHERE pclass = 2;

SELECT AVG(age) as p3_ave_age
FROM titanic_table
WHERE pclass = 3;

#--6. What was the average fare by passenger class? By survival?
#-- p1_ave_fare = 84.1546875, p2_ave_fare = 20.6621831, p3_ave_fare = 13.7077073
#-- surv_ave_fare = 48.3954076023391813 , died_ave_fare = 22.2085840366972477

SELECT AVG(fare) as p1_ave_fare
FROM titanic_table
WHERE pclass = 1;

SELECT AVG(fare) as p2_ave_fare
FROM titanic_table
WHERE pclass = 2;

SELECT AVG(fare) as p3_ave_fare
FROM titanic_table
WHERE pclass = 3;

SELECT AVG(fare) as surv_ave_fare
FROM titanic_table
WHERE survived = 1;

SELECT AVG(fare) as surv_ave_fare
FROM titanic_table
WHERE survived = 0;

#--7. How many siblings/spouses aboard on average, by passenger class? By survival?
#-- p1_ave_ss = 0.416667, p2_ave_ss = 0.40217391304 , p3_ave_ss = 0.620123203
#-- surv_ave_ss= 0.47368421052631578947, died_ave_ss = 0.55779816513761467890

SELECT AVG(siblingspouseaboard) as p1_ave_ss
FROM titanic_table
WHERE pclass = 1;

SELECT AVG(siblingspouseaboard) as p2_ave_ss
FROM titanic_table
WHERE pclass = 2;

SELECT AVG(siblingspouseaboard) as p3_ave_ss
FROM titanic_table
WHERE pclass = 3;

SELECT AVG(siblingspouseaboard) as surv_ave_ss
FROM titanic_table
WHERE survived = 1;

SELECT AVG(siblingspouseaboard) as died_ave_ss
FROM titanic_table
WHERE survived = 0;

#--8. How many parents/children aboard on average, by passenger class? By survival?
#-- p1_ave_pc = 0.35648148148148148148, p2_ave_pc = 0.380434782608695, p3_ave_pc = 00.39630390143
#-- surv_ave_pc= 0.46491228070175438596, died_ave_pc = 0.33211009174311926606

SELECT AVG(parentschildrenaboard) as p1_ave_pc
FROM titanic_table
WHERE pclass = 1;

SELECT AVG(parentschildrenaboard) as p2_ave_pc
FROM titanic_table
WHERE pclass = 2;

SELECT AVG(parentschildrenaboard) as p3_ave_pc
FROM titanic_table
WHERE pclass = 3;


SELECT AVG(parentschildrenaboard) as surv_ave_pc
FROM titanic_table
WHERE survived = 1;


SELECT AVG(parentschildrenaboard) as died_ave_pc
FROM titanic_table
WHERE survived = 0;

#--9. Do any passengers have the same name? 
#-- total names = 887, distint names count = 887
#-- therefore zero common name

SELECT count( DISTINCT NAME) 
FROM titanic_table;

SELECT count(NAME) 
FROM titanic_table

'''


result1 = CURSOR_titanic.execute(query1).fetchone()
print('')
print(f'1. Survival Count, {result1}')


CONNECTION_titanic.commit()
CURSOR_titanic.close()
CONNECTION_titanic.close()



"""
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

  """