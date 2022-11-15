-- select * from language;
-- select * from customer_review;

-- update film
-- set language_id = '5' where film_id = '1'
-- update film
-- set language_id = '3' where film_id = '2'

-- store_id and address_id are connected as references.
-- the numbers are picked according to the reference id's, 
-- so can be in random order depending on the input

-- select count(*) from rental where return_date is null;


-- select title from film
-- join film_actor on film_actor.film_id = film.film_id
-- where fulltext @@ to_tsquery('sumo')
-- and actor_id = (select actor_id from actor where first_name ='Penelope' and last_name = 'Monroe');

-- select title from film
-- join film_category on film.film_id = film_category.film_id
-- where category_id = 6
-- and length < 60
-- and rating = 'R';

-- select film.title from film on film.film_id = inventory.film_id
-- join rental on rental.inventory_id = inventory.inventory_id
-- join customer on rental.customer_id = customer.customer_id
-- where first_name = 'Matthew' and last_name = 'Mahan' 
-- and rental_rate > 4
-- and rental.return_date between '28/07/2005' and '01/08/2005';



-- SELECT film.title, customer.first_name, customer.last_name,
-- payment.payment_id,payment.amount,return_date
-- FROM rental JOIN customer
-- ON rental.customer_id = customer.customer_id
-- JOIN payment ON rental.rental_id = payment.rental_id
-- JOIN inventory ON rental. inventory_id = inventory.inventory_id
-- JOIN film ON inventory. film_id = film.film_id
-- WHERE customer. first_name = 'Matthew'
-- AND customer. last_name = 'Mahan'
-- AND rental.return_date < '2005-08-01'
-- AND rental.return_date > '2005-07-28'
-- AND payment.amount > 4;


-- SELECT film.title, film.description, film. replacement_cost
-- FROM film
-- JOIN inventory
-- ON film. film_id = inventory.film_id
-- JOIN rental
-- ON rental. inventory_id = inventory. inventory_id
-- JOIN customer
-- ON rental. customer_id = customer.customer_id
-- where customer .first_name = 'Matthew'
-- and customer.last_name = 'Mahan'
-- and film. title like '%Boat%'
-- or film.description like '%Boat%'
-- order by film.replacement_cost desc
-- limit 1