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

select count (*) from Customer_profile where isLoggedIn='false'