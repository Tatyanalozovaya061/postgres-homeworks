-- SQL-команды для создания таблиц
CREATE TABLE customers(
	customer_id char(5) PRIMARY KEY,
	company_name varchar(100) not null,
	contact_name varchar(100) not null
);

CREATE TABLE employees(
	employee_id int PRIMARY KEY,
	first_name varchar(100) not null,
	last_name varchar(100) not null,
	title varchar(100) not null,
	birth_date date not null,
	notes text not null
);

CREATE TABLE orders(
	order_id int PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date not null,
	ship_city varchar(100) not null
);

SELECT * FROM orders;
