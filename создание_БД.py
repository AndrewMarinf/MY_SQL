
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
            create_table_query = "CREATE DATABASE my_db_test"
            cursor.execute(create_table_query)
            print("Table created successfully")

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)