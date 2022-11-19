import requests
import psycopg2

url = 'https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population'

data = requests.get(url).json()
# print(type(data))

# # print (data [0]['name']['common'])

# countries_names = [country['name']['common'] for country in data]

# print(countries_names)

print (data [0])
name = data[0]['name']['common']
capital = data[0]['capital'][0]
subregion = data[0]['subregion']
flag = data[0]['flag']
population = data[0]['population']

print (name,capital,subregion,flag,population)


# connect:


HOSTNAME =  'localhost'
USERNAME =  'postgres'
PASSWORD =  'Sg102030'
DATABASE =  'country'

connection = psycopg2.connect(host =HOSTNAME, user =USERNAME, password = PASSWORD, dbname =DATABASE)

cursor = connection.cursor()
q = "SELECT * from countries;" 

cursor.execute(q)

results = cursor.fetchall()
print(results)

# connection.close()



# insert:

cursor = connection.cursor()

new_row = ('Sarahland', 'GG', 'pascomprisckoi', 1212, 5555)

q = f"INSERT INTO countries (name, capital, subregion, flag, population)values {new_row};"

cursor.execute(q)

connection.commit()

connection.close()