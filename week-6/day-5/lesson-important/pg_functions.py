# creer une fonction pour automatisier l'insertion

import psycopg2

HOSTNAME =  'localhost'
USERNAME =  'postgres'
PASSWORD =  'Sg102030'
DATABASE =  'daily-w6d4'


# function for runnig queries
def run_query(q, mode):
    # available modes = s-SELECT, m-MODIFY
    
    connection = psycopg2.connect(host =HOSTNAME, user =USERNAME, password = PASSWORD, dbname =DATABASE)
    cursor = connection.cursor()
    cursor.execute(q)

    # selecting/get stuff
    if mode == 's':
        results = cursor.fetchall()

    # modifying/ post stuff
    if mode == 'm':
        connection.commit()
        results = connection.commit()


    connection.close()
    return results


# essaies selectionner une colonne:

q = "SELECT * from items;" 
# run_query(q, 's')
# print(run_query(q, 's'))

q2 = "SELECT name from items"
print(print(run_query(q2, 's')))


# essaies ajouter une ligne:

new_row = "(5, 'apple', 30)"
q3 = f"INSERT INTO items (id, name, price)values {new_row};"
run_query(q3, 'm')