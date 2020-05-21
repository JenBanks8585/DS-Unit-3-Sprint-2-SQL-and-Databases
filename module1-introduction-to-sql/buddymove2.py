'''
DRAFT for df.to_sql route


import os
import sqlite3
import pandas as pd
import csv

conn = sqlite3.connect("buddymove_holidayiq.sqlite3")
df = pd.read_csv(r'C:\Users\J8015\Desktop\Repo\DS-Unit-3-Sprint-2-SQL-and-Databases\module1-introduction-to-sql\buddymove_holidayiq.csv')
df.to_sql("review1", conn)
cursor1 = conn.cursor()

query1 = """

SELECT count(Sports)
FROM review1
"""
result1 = cursor.execute(query1).fetchone()
print('')
print(f'1. Count how many rows you have?, {result1}')

'''