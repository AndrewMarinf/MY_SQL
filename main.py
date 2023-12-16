import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print('successfully connected...')
    print('#' * 20)
    try:
        with connection.cursor() as cursor:
            create_table_queries = [
                "CREATE TABLE Bicycle(ID int PRIMARY KEY AUTO_INCREMENT, "
                "Brand varchar(20) not null, "
                "password varchar(32), "
                "RentPrice int not null);",

                "CREATE TABLE Client(ID int PRIMARY KEY AUTO_INCREMENT, "
                "Name varchar(10) not null, "
                "Passport varchar(50) not null, "
                "Country varchar(50) not null);",
                
                "CREATE TABLE RentBook( ID int PRIMARY KEY AUTO_INCREMENT, "
                "Date date not null, "
                "Time int not null, "
                "Paid bit not null, "
                "BicycleID int not null, "
                "ClientID int not null, "
                "FOREIGN KEY (BicycleID) REFERENCES Bicycle (ID), "
                "FOREIGN KEY (ClientID) REFERENCES Client (ID));"
            ]
            for query in create_table_queries:
                cursor.execute(query)
            print("Tables created successfully")
    finally:
        connection.close()
except Exception as ex:
    print('Connection refused...')
    print(ex)
