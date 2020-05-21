import os
import sqlite3
import pandas as pd

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "rpg_db.sqlite3")

connection = sqlite3.connect(DB_FILEPATH)
print("CONNECTION:", connection)

cursor = connection.cursor()
#print("CURSOR", cursor)


# 1. How many total Characters are there? 

query1 = """
SELECT 
    COUNT(DISTINCT character_id)
FROM charactercreator_character
"""
result1 = cursor.execute(query1).fetchall()
print('')
print(f'1. How many total Characters are there?, {result1}')


# 2. How many total Items? 

query2a = """
    SELECT 
        COUNT(DISTINCT cm.character_ptr_id)
    FROM charactercreator_mage as cm
"""
result2a = cursor.execute(query2a).fetchall()
print(f'2a. Number of mages, {result2a}')

query2b = """
    SELECT 
        COUNT(DISTINCT ccn.mage_ptr_id)
    FROM charactercreator_necromancer as ccn
"""
result2b = cursor.execute(query2b).fetchall()
print(f'2b. Number of mage_necromancer, {result2b}')

query2c = """
    SELECT 
        COUNT(DISTINCT ct.character_ptr_id)
    FROM charactercreator_thief as ct 
"""
result2c = cursor.execute(query2c).fetchall()
print(f'2c. Number of thieves, {result2c}')

query2d = """
    SELECT 
        COUNT(DISTINCT cc.character_ptr_id)        
    FROM charactercreator_cleric as cc 
"""
result2d = cursor.execute(query2d).fetchall()
print(f'2d. Number of mage_necromancer, {result2d}')

query2e = """
     SELECT 
        COUNT(DISTINCT cf.character_ptr_id)
    FROM charactercreator_fighter as cf 
"""
result2e = cursor.execute(query2e).fetchall()
print(f'2e. Number of fighters, {result2e}')


# 3. How many total Items? 

query3 = """
SELECT 
COUNT(item_id)
FROM armory_item
"""
result3 = cursor.execute(query3).fetchall()
print(f'3. How many total Items?, {result3}')

# 4. How many of the Items are weapons? How many are not?? 

query4a = """
    SELECT 
        COUNT(item_ptr_id)
    FROM armory_weapon
"""
result4a = cursor.execute(query4a).fetchall()
print(f'4a. How many of the Items are weapons?, {result4a}')

query4b = """
    SELECT
    ((SELECT COUNT(item_id)
    FROM armory_item) 
    -
    (SELECT COUNT(item_ptr_id)
    FROM armory_weapon))
"""
result4b = cursor.execute(query4b).fetchall()
print(f'4b. How many of the Items are NOT weapons?, {result4b}')

# 5. How many Items does each character have? (Return first 20 rows) 

query5 = """
    SELECT
        ccc.character_id,
        ccc.name,
        count(cci.item_id) as item_count_per_char
    FROM
        charactercreator_character as ccc
    LEFT JOIN charactercreator_character_inventory as cci 
        on ccc.character_id = cci.character_id
    LEFT JOIN armory_item as ai 
        on cci.item_id = ai.item_id
    GROUP by
        ccc.character_id
    ORDER BY
        item_count_per_char DESC
    LIMIT
        20
"""
cols= ['character_id', 'name', 'itemcount_per_char']
result5 = pd.DataFrame(data=cursor.execute(query5).fetchall(), columns = cols)
print('5. How many Items does each character have? (Return first 20 rows)')
print('')
print(result5)

# 6. How many Weapons does each character have? (Return first 20 rows) 

query6 = """

  SELECT
        ccc.character_id,
        ccc.name,
        count(aw.item_ptr_id) as weapon_per_char
    FROM
        charactercreator_character as ccc
    LEFT JOIN charactercreator_character_inventory as cci 
        on ccc.character_id = cci.character_id
    LEFT JOIN armory_item as ai 
        on cci.item_id = ai.item_id
    LEFT JOIN armory_weapon as aw 
        on ai.item_id = aw.item_ptr_id
    GROUP by
        ccc.character_id
    ORDER BY
        weapon_per_char DESC
    LIMIT
        20
"""
cols= ['character_id', 'name', 'weaponcount_per_char']
result6 = pd.DataFrame(data=cursor.execute(query6).fetchall(), columns = cols)
print('')
print('6. How many Weapons does each character have? (Return first 20 rows)')
print('')
print(result6)

# 7. On average, how many Items does each Character have?

query7 = """

     SELECT AVG(item_count_per_char) as avg_itemcount
     FROM(
     SELECT
        ccc.character_id,
        ccc.name,
        count(cci.item_id) as item_count_per_char
     FROM
        charactercreator_character as ccc
     LEFT JOIN charactercreator_character_inventory as cci 
        on ccc.character_id = cci.character_id
     LEFT JOIN armory_item as ai 
        on cci.item_id = ai.item_id
     GROUP by
        ccc.character_id
        )
"""
result7 = cursor.execute(query7).fetchall()
print('')
print(f'7. On average, how many Items does each Character have?, {result7}')

# 8. On average, how many Weapons does each character have? 

query8 = """

    SELECT AVG(weapon_per_char) as avg_weapon
    FROM (
    SELECT
        ccc.character_id,
        ccc.name,
        count(aw.item_ptr_id) as weapon_per_char
    FROM
        charactercreator_character as ccc
    LEFT JOIN charactercreator_character_inventory as cci 
        on ccc.character_id = cci.character_id
    LEFT JOIN armory_item as ai 
        on cci.item_id = ai.item_id
    LEFT JOIN armory_weapon as aw 
        on ai.item_id = aw.item_ptr_id
    GROUP by
        ccc.character_id)
"""
result8 = cursor.execute(query8).fetchall()
print(f'8. On average, how many Weapons does each character have? , {result8}')
print('')