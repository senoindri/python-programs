create database assignment2;
use assignment2;

create table employees(
employee_id int primary key,
name varchar(30),
department_id int,
salary float,
hire_data date,
manager_id int);
insert into employees values 
(401,"anandi",3,50000,'1990-08-01',101),
(402,"maitree",4,45000,'2010-05-04',102),
(403,"kamala",4,35000,'2013-09-07',102),
(404,"aditri",2,12000,'2020-10-01',100),
(405,"ryan",3,10000,'2000-09-03',101),
(406,"praveen",3,12000,'2019-10-10',103);

create table departments(
department_id int primary key,
department_name varchar(20),
location varchar(20));
insert into departments values 
(4,"frontend","banglore"),
(3,"backend","kolkata"),
(2,"dbms","hyderabad");

create table customers(
customer_id int primary key,
name varchar(20),
email varchar(20),
phone varchar(10));
insert into customers values
(10,"malika","malik@gmail.com","9878789900"),
(11,"komal","kom@gmail.com","9223344554"),
(12,"dhwani","dhwn@gmail.com","9455440040"),
(13,"prarthna","pgrth@gmail.com","855667796"),
(14,"yesly","ysl@gmail.com","8420410966");

create table suppliers(
supplier_id int primary key,
name varchar(20),
email varchar(20),
phone varchar(10));
insert into suppliers values 
(30,"aws","aws@gmail.com","3323356885"),
(31,"meta","meta@gmail.com","3342228987"),
(32,"apple","apple@gmail.com","3304442090"),
(33,"google","google@gmail.com","3323432454"),
(34,"netflix","netflix@gmail.com","3345657898");

create table orders(
order_id int primary key,
customer_id int,
foreign key (customer_id) references customers(customer_id),
order_date date);
insert into orders values
(201,10,'2025-02-01'),
(202,11,'2025-03-02'),
(203,12,'2025-04-05'),
(204,13,'2025-05-20'),
(205,14,'2025-06-17');

create table order_details(
order_detail_id int primary key,
order_id int,
foreign key (order_id) references orders(order_id),
product_id int,
foreign key (product_id) references products(product_id),
quantity float,
unit_prince float);
insert into order_details values
(601,201,502,5,2000),
(602,202,501,1,40000),
(603,203,504,2,14000),
(604,204,503,4,2400),
(605,205,505,1,25000);

create table products(
product_id int primary key,
product_name varchar(20),
category_id int,
unit_price float,
stock int);
insert into products values 
(501,"computers",51,40000,500),
(502,"dvds",52,5000,400),
(503,"earphones",53,600,200),
(504,"keyboards",54,7000,500),
(505,"phones",55,25000,600);

create table categories(
category_id int primary key,
category_name varchar(20));
insert into categories values 
(701,"hardware"),
(702,"software"),
(703,"middleware"),
(704,"helpers");

create table sales(
sale_id int primary key,
product_id int,
foreign key (product_id) references products(product_id),
sale_date date,
quantity_sold int,
total_revenue float);
insert into sales values
(801,501,'2025-02-01',1,40000),
(802,502,'2025-03-02',5,2500),
(803,503,'2025-04-05',4,800),
(804,504,'2025-05-20',3,1500),
(805,505,'2025-06-17',2,50000);

create table leaves(
leave_id int primary key,
employee_id int,
foreign key (employee_id) references employees(employee_id),
leave_start_date date,
leave_end_dated date);
insert into leaves values
(901,401,'2025-01-05','2025-01-08'),
(902,402,'2025-02-02','2025-02-20'),
(903,403,'2025-03-10','2025-03-31'),
(904,404,'2025-04-06','2025-05-01'),
(905,405,'2025-05-02','2025-05-08'),
(906,406,'2025-05-16','2025-05-26');

create table experience(
employee_id int primary key,
foreign key (employee_id) references employees(employee_id),
years_of_exeprience int);
insert into experience values 
(401,25),
(402,15),
(403,12),
(404,5),
(405,25),
(406,6);

#Retrieve the names of employees and their department names from Employees and Departments tables.
SELECT e.name AS employee_name, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id;

#Get a list of all customers and the orders they have placed. Include customers with no orders
SELECT c.name AS customer_name, o.order_id, o.order_date
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id;

#Find the total revenue generated per product from the OrderDetails table.
SELECT p.product_name, SUM(od.quantity * od.unit_prince) AS total_revenue
FROM order_details od
JOIN products p ON od.product_id = p.product_id
GROUP BY p.product_id, p.product_name;

#ind employees whose salary is greater than the average salary of their department
SELECT e.name, e.salary, e.department_id
FROM employees e
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM employees e2
    WHERE e2.department_id = e.department_id);

#List customers who placed an order for the product with the highest unit price 
SELECT DISTINCT c.name AS customer_name
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
WHERE od.product_id = (
    SELECT product_id
    FROM products
    ORDER BY unit_price DESC
    LIMIT 1
);

#Get a list of all customers and suppliers in one list with their names and contact info
SELECT name, email, phone, 'Customer' AS type
FROM customers
UNION ALL
SELECT name, email, phone, 'Supplier' AS type
FROM suppliers;

#For each category, show the most expensive product and its price
SELECT c.category_name, p.product_name, p.unit_price
FROM categories c
JOIN products p ON c.category_id = p.category_id
WHERE (p.unit_price, p.category_id) IN (
    SELECT MAX(p2.unit_price), p2.category_id
    FROM products p2
    GROUP BY p2.category_id
);