import psycopg2
conn=psycopg2.connect(dbname="postgres", user="postgres", password="millie578", host="localhost", port="5432")
print("Connection established successfully")
cursor=conn.cursor()

#CREATING A TABLE
def create_table():
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (name text, age integer, id integer);''')
    print("Table created successfully")

conn.commit()
create_table()

#INSERTING DATA INTO THE TABLE
def insert_data():
    cursor.execute('''INSERT INTO users (name, age, id) VALUES ('Anna', 12, 01);''')
    cursor.execute('''INSERT INTO users (name, age, id) VALUES ('Bob', 25, 02);''')
    print("Data inserted successfully")

conn.commit()
insert_data()

#FETCHING AND DISPLAYING DATA FROM THE TABLE
def display_data():
    cursor.execute('''SELECT * FROM users''')
    for row in cursor.fetchall():
        print(row)

conn.commit()
display_data()

#USER INPUT FOR DATA INSERTION
def user_input():
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    id = int(input("Enter id: "))
    cursor.execute('''INSERT INTO users (name, age, id) VALUES (%s, %s, %s)''', (name, age, id))
    print("Data inserted successfully")
    print("Current data in the table:")
    display_data()
conn.commit()
user_input()

#SELECT, WHERE, TRUNCATE
def select_where_truncate():
    cursor.execute('''SELECT * FROM users WHERE age > 20''')
    print("Users older than 20:")
    for row in cursor.fetchall():
        print(row)
    
    cursor.execute('''TRUNCATE TABLE users''')
    print("Table truncated successfully")
    conn.commit()
select_where_truncate()
display_data()

#DROP TABLE
def drop_table():
    cursor.execute('''DROP TABLE IF EXISTS users''')
    print("Table dropped successfully")

conn.close()



