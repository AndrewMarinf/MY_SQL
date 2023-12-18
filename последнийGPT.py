import random
import mysql.connector

# Подключение к базе данных MySQL
db = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="yourdatabase"
)

# Создание курсора
cursor = db.cursor()

# Создание таблицы Client
cursor.execute("CREATE TABLE IF NOT EXISTS Client ("
               "passport varchar(11) PRIMARY KEY, "
               "full_name varchar(250), "
               "country varchar(100))")

# Генерация и вставка 10000 значений в таблицу
for _ in range(10000):
    passport1 = random.randint(1000, 9999)
    passport2 = random.randint(100000, 999999)
    passport = str(passport1) + " " + str(passport2)
    full_name = random.choice(["John Smith", "Jane Johnson", "Michael Brown", "Emma Davis", "David Miller"])
    country = random.choice(["USA", "Canada", "UK", "Germany", "France"])
    query = "INSERT INTO Client (passport, full_name, country) VALUES (%s, %s, %s)"
    values = (passport, full_name, country)
    cursor.execute(query, values)

# Подтверждение изменений и закрытие соединения
db.commit()
cursor.close()
db.close()

print("Данные успешно записаны в таблицу Client.")