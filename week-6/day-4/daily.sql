-- create table product_orders (
-- id serial primary key,
-- quantity int
-- );

-- insert into product_orders values
-- ((select id from items where name = 'banana'),5) ,
-- ((select id from items where name = 'mango'),8),
-- ((select id from items where name = 'chocolat'),2);


-- create table items (
-- id serial primary key,
-- name varchar(50),
-- price float
-- );


-- select *
-- from product_orders
-- inner join items
-- 	on product_orders.id = items.id

-- insert into items(name, price) values
-- ('chocolat', 10),
-- ('banana', 5),
-- ('mango',15);

-- create or replace function total ( int, user_name varchar)
-- returns int AS $total_price$
-- declare total int;
-- begin


create or replace function get_price_by_id(given_id int)
 returns int as $priceOfOrder$
begin
 return( select price
    from product_orders as p
    inner join items as i
    on p.item_id = i.item_id
    where p.order_id = given_id);
end;



