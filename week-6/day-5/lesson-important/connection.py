# connecter une data base sql avec python 

import psycopg2

HOSTNAME =  'localhost'
USERNAME =  'postgres'
PASSWORD =  'Sg102030'
DATABASE =  'daily-w6d4'

connection = psycopg2.connect(host =HOSTNAME, user =USERNAME, password = PASSWORD, dbname =DATABASE)

# cursor for runnig queries
cursor = connection.cursor()

# items = un tableau dans daily-w6d4
q = "SELECT * from items;" 
# run query
cursor.execute(q)

# get the data from cursor
results = cursor.fetchall()
print(results)

connection.close()