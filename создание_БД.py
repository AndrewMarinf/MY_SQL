
import pymysql
try:
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='9945',
        database='sys',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        # create table
        with connection.cursor() as cursor:
            create_table_query = "CREATE DATABASE TEST_300"
            cursor.execute(create_table_query)
            print("Table created successfully")

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)



# CREATE TABLE Client_ (
# id SERIAL PRIMARY KEY,
# name VARCHAR(255)
# );

# CREATE TABLE Orders_ (
# id SERIAL PRIMARY KEY,
# client_id_ INTEGER,
# price NUMERIC(10,2),
# FOREIGN KEY (client_id_) REFERENCES Client_(id)
# );

# INSERT INTO Client_ (name) VALUES ('John Doe');
# INSERT INTO Client_ (name) VALUES ('Jane Smith');
# INSERT INTO Client_ (name) VALUES ('Mark Johnson');
# INSERT INTO Client_(name) VALUES ('Sarah Wilson');
# INSERT INTO Client_ (name) VALUES ('Michael Brown');

# INSERT INTO Orders_ (client_id_, price) VALUES (1, 100.00);
# INSERT INTO Orders_ (client_id_, price) VALUES (1, 200.00);
# INSERT INTO Orders_ (client_id_, price) VALUES (2, 150.00);
# INSERT INTO Orders_ (client_id_, price) VALUES (3, 75.50);
# INSERT INTO Orders_ (client_id_, price) VALUES (5, 300.00);    

