import os
import sqlite3
import pandas as pd

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.db")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

query1 = """

SELECT count(Sports)
FROM buddymove_holidayiq
"""
result1 = cursor.execute(query1).fetchone()
print('')
print(f'1. Count how many rows you have?, {result1}')

# 2. How many total Items? 

query2 = """
SELECT count(Shopping)
FROM buddymove_holidayiq as bh
WHERE bh.Nature >= 100
AND bh.Shopping >= 100
"""
result2 = cursor.execute(query2).fetchone()
print(f'2. Nature & Shopping >= 100, {result2}')

# 3. (Stretch) What are the average number of reviews for each category? 

query3a = """
SELECT avg(Shopping)
FROM buddymove_holidayiq 
"""
query3b = """
SELECT avg(Sports)
FROM buddymove_holidayiq 
"""
query3c = """
SELECT avg(Religious)
FROM buddymove_holidayiq 
"""
query3d = """
SELECT avg(Nature)
FROM buddymove_holidayiq 
"""
query3e = """
SELECT avg(Picnic)
FROM buddymove_holidayiq 
"""
query3f = """
SELECT avg(Theatre)
FROM buddymove_holidayiq 
"""
result3a = cursor.execute(query3a).fetchone()
result3b = cursor.execute(query3b).fetchone()
result3c = cursor.execute(query3c).fetchone()
result3d = cursor.execute(query3d).fetchone()
result3e = cursor.execute(query3e).fetchone()
result3f = cursor.execute(query3f).fetchone()
print(f'3a Average num reviews for Shopping, {result3a}')
print(f'3b Average num reviews for Sports, {result3b}')
print(f'3c Average num reviews for Religious, {result3c}')
print(f'3d Average num reviews for Nature, {result3d}')
print(f'3e Average num reviews for Picnic, {result3e}')
print(f'3f Average num reviews for Theatre, {result3f}')