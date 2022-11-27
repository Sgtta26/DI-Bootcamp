-- CREATE TABLE Customer(
-- id serial PRIMARY KEY NOT NULL,
-- first_name VARCHAR (30),
-- last_name VARCHAR (30) NOT NULL
-- );

-- CREATE TABLE Customer_profile(
-- id serial primary key NOT NULL,
-- isLoggedIn BOOLEAN DEFAULT(FALSE),
-- customer_id int NOT NULL,
-- FOREIGN KEY (customer_id) REFERENCES Customer (id)
-- );

-- Insert into Customer(first_name, last_name) VALUES
-- ('John', 'Doe'),
-- ('Jerome', 'Lalu'),
-- ('Lea', 'Rive');

-- Insert into Customer_profile (isLoggedIn, customer_id)
-- select 'false', id from customer where first_name ILIKE 'John';

-- Insert into Customer_profile (isLoggedIn, customer_id)
-- select 'true', id from customer where first_name ILIKE 'Jerome'
-- select customer_id, first_name from Customer
-- join customer_profile on Customer.id=Customer_profile.customer_id
-- select customer_id, isLoggedIn, first_name from Customer
-- left_join Customer_profile on Customer.id=Customer_profile.customer_id

-- select count (*) from Customer_profile where isLoggedIn='false'

-- create table book (
-- book_id serial primary key, 
-- title varchar (200) not null,
-- author varchar(200) not null); 

-- insert into book (title,author) values 
-- ('Alice In Wonderland', 'Lewis Carroll'),
-- ('Harry Potter', 'J.K Rowling'),
-- ('To kill a mockingbird', 'Harper Lee');

-- create table student (
-- student_id serial primary key, 
-- name varchar(200) not null,
-- age int, check (age < 15));

-- insert into student (name,age) values 
-- ('John', 12),
-- ('Lera', 11),
-- ('Patrick', 10),
-- ('Bob', 14);


-- create table library (
-- book_id int references book(book_id) ON UPDATE CASCADE, 
-- student_id int references student(student_id) ON UPDATE CASCADE, 	
-- borrowed_date date,
-- primary key (book_id, student_id)); 


-- insert into library(book_id, student_id, borrowed_date) values
--   ((select book_id from book where title='Alice In Wonderland'),
--   (select student_id from student where name='John'), '2022-02-15'),

--  ((select book_id from book where title='To kill a mockingbird'),
--   (select student_id from student where name='Bob'), '2021-03-03'),
 
--  ((select book_id from book where title='Alice In Wonderland'),
--  (select student_id from student where name='Lera'), '2021-05-23'),
 
--  ((select book_id from book where title='Harry Potter'), 
--  (select student_id from student where name='Bob'), '2021-08-12');


select * from library join book
on library.book_id = book.book_id
join student on library.student_id = student.student_id;