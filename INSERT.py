import random
import pymysql
# from passport_ import passport
# from fisrst_last_ import generate_random_person
# from country import country
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
        # старый код
        # with connection.cursor() as cursor:
        #     # insert_query = "INSERT INTO `Client` (name, password, Country) VALUES ('Anna', {passport}, 'anna@gmail.com');" не рабочая
        #     # insert_query = "INSERT INTO `Client (name, password, Country) VALUES (%s, %s, %s)", (generate_random_person, passport, country) 1 ВРИК
        #     insert_query = "INSERT INTO `Client (name, password, Country) VALUES ('{}','{}', '{}');".format(generate_random_person, passport, country)
        #     # insert_query = "INSERT INTO Client (name, password, Country) VALUES ('Anna', '{}', 'anna@gmail.com');".format(passport)
        #     cursor.execute(insert_query)
        #     connection.commit()
        #     print("Data Inserted into the table")

    #    новый код 
        # with connection.cursor() as cursor:
        #     for i in range(1,10000 + 1):
        #         insert_query = "INSERT INTO `Client` (Name, Password, Country) VALUES (%s, %s, %s)" 
        #         velues = (generate_random_person(), passport(), country())
        #         cursor.execute(insert_query,velues)
        #         connection.commit()
        #         print("Data Inserted into the table")

        # 3 варик GPT
        with connection.cursor() as cursor:
            for _ in range(10000):
                passport1 = random.randint(1000, 9999)
                passport2 = random.randint(100000, 999999)
                passport = str(passport1) + " " + str(passport2)
                full_name = random.choice(["John Smith", "Jane Johnson", "Michael Brown", "Emma Davis", "David Miller"])
                country = random.choice(["USA", "Canada", "UK", "Germany", "France"])
                query = "INSERT INTO `Client` (Name, Passport , Country) VALUES (%s, %s, %s)"
                values = (full_name , passport, country )
                cursor.execute(query, values)
                connection.commit()
                print("Data Inserted into the table")

    finally:
        connection.close()
except Exception as ex:
    print('Connection refused...')
    print(ex)

