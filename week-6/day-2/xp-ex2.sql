-- select * from customer;

-- select first_name as full_name, last_name as full_name from customer;

-- select distinct create_date from customer;

-- select * from customer order by first_name DESC;

-- select film_id, title, description, release_year, rental_rate from film;

-- select address, phone from address where district = 'Texas' ;

-- select * from film where film_id = 15 or film_id = 150;

-- select film_id, title, description, length, replacement_cost from film;

-- select film_id, title, description, length, replacement_cost from film where (title like 'S%');

-- select replacement_cost from film where replacement_cost=(select min(replacement_cost)from film) Limit 10;

-- select replacement_cost from film where replacement_cost=(select min(replacement_cost)from film) Limit 20;

-- select customer.customer_id, customer.first_name, customer.last_name as full_name, payment.amount, payment.payment_date from customer inner join payment on payment.customer_id = customer.customer_id order by customer.customer_id;

-- select customer.customer_id, customer.first_name, customer.last_name, payment.payment_date, payment.amount
-- from customer inner join payment on payment.customer_id = customer.customer_id
-- order by customer.customer_id ASC;

select * from film join inventory on film.film_id=inventory.film_id where film.film_id not in (inventory.film_id);
select city.city, country.country from city join country on city.country_id = country.country_id;

