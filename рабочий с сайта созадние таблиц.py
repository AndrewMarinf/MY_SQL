
import pymysql

try:
    connection = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        user='root',
        password='9945',
        database='TEST_300',
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        # create table
        with connection.cursor() as cursor:
            create_table_query = "CREATE TABLE `Clients`(id int AUTO_INCREMENT," \
                            " name varchar(32)," \
                            " password varchar(32)," \
                            " email varchar(32), PRIMARY KEY (id));"
            cursor.execute(create_table_query)
            print("Table created successfully")

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)