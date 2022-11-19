# inserrer une ligne dans un tableau

import psycopg2

HOSTNAME =  'localhost'
USERNAME =  'postgres'
PASSWORD =  'Sg102030'
DATABASE =  'daily-w6d4'

connection = psycopg2.connect(host =HOSTNAME, user =USERNAME, password = PASSWORD, dbname =DATABASE)

# cursor for runnig queries:
cursor = connection.cursor()

# add new row:
new_row = "(4, 'kiwi', 20)"

# our query:
q = f"INSERT INTO items (id, name, price)values {new_row};"

# run query:
cursor.execute(q)

# pour que la new_row apparaisse:/ make the update:
connection.commit()

connection.close()