import random

def passport():
    passport_numbers = []

# # Генерируем 10000 значений паспортных номеров
#     for i in range(10000):
#         first_part = random.randint(1000, 9999)
#         second_part = random.randint(100000, 999999)
#         full_passport_no = str(first_part) + ' ' + str(second_part)
#         passport_numbers.append(full_passport_no)
#         for passport_no in passport_numbers:
#             return passport_no         


    first_part = random.randint(1000, 9999)
    second_part = random.randint(100000, 999999)
    full_passport_no = str(first_part) + ' ' + str(second_part)
    passport_numbers.append(full_passport_no)
    for passport_no in passport_numbers:
        return passport_no
      


