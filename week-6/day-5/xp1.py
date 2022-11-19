import psycopg2

HOSTNAME =  'localhost'
USERNAME =  'postgres'
PASSWORD =  '11111'
DATABASE =  'd5menu'


class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def run_query(self, query):
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()


    def save(self):
        query = f"INSERT INTO menu (name, price) VALUES ('{self.name}', {self.price})"
        self.run_query(query)
    
    def delete(self):
        query = f"DELETE FROM menu where name = '{self.name}'"
        self.run_query(query)
        
    def update(self, old_name):
        query = f"update menu set name = '{self.name}' where name = '{old_name}'"
        self.run_query(query)
        query = f"update menu set price = {self.price} where name = '{self.name}'"
        self.run_query(query)

    def all():
        query = "select * from menu"
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        connection.close()
    

    def get_by_name(get_name):
        query = f"select name from menu where name ='{get_name}'"
        connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
        cursor = connection.cursor()
        cursor.execute(query)
        # connection.commit()
        results = cursor.fetchall()
        connection.close()
        if results:
            return results
        print('No')
# MenuItem.all()

MenuItem.get_by_name('Pa')




pizza = MenuItem('Pizza', 30)
burger = MenuItem('burger', 35)


MenuItem.update(pizza, 'burger')

# MenuItem.save(burger)
# MenuItem.delete(burger)

