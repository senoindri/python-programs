create database assignment1;
use assignment1;
create table employees(
id int primary key,
name varchar(100),
department varchar(100),
salary int,
joining_date date);
insert into employees values 
(101,"dev","it",65000,'2000-02-03'),
(102,"kapil","eng",20000,'2014-01-02'),
(103,"john","math",70020,'2010-09-05'),
(104,"mia","it",70000,'1990-09-20'),
(105,"drew","it",50000,'2024-05-06');
select * from employees;
select name from employees where department="it" AND salary>60000;
select * from employees order by salary desc;
insert into employees values (106,"clara","math",50000,'2000-09-08'),(107,"john","eng",30000,'1999-01-02');
select department, avg(salary) as avg_sal from employees group by department;