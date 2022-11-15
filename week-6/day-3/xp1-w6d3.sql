-- select title, description, name
-- from film
-- join language
-- on film.language_id = language.language_id;

-- select title, description, name
-- from film
-- left join language
-- on film.language_id = language.language_id;

-- select title, description, name
-- from film
-- right join language
-- on film.language_id = language.language_id;

-- create table new_film (
-- id int primary key,
-- name varchar(50)
-- );

-- create table customer_review (
-- 	review_id SERIAL not null,
-- 	film_id int not null,
-- 	language_id int ,
-- 	title varchar(50),
-- 	score int ,
-- 	review_text text,
-- 	last_update timestamp,
-- 	primary key (review_id), constraint fk_film_id
-- 	foreign key (film_id)
-- 		references new_film (id)
-- 		on delete cascade,
-- foreign key (language_id)
-- references language (language_id)
-- );

-- insert into new_film(id, name) values
-- (1, 'chocolat'),
-- (2, 'banana');

-- select * from customer_review;
-- select * from new_film;

-- delete from new_film where id =1;

-- select * from customer_review; ==> it's empty