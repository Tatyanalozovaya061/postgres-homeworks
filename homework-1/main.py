"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

# подключаемся с бд
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='1111')
# создаем курсор
cur = conn.cursor()

# считываем данные из csv и переносим в бд
with open('north_data/customers_data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cur.execute('INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)',
                    (row['customer_id'], row['company_name'], row['contact_name']))

with open('north_data/employees_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s)",
                    (row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes']))

with open('north_data/orders_data.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        cur.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
                    (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city'],))

conn.commit()
conn.close()
