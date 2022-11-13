create table item (
id int primary key,
desk varchar(50),
price float
);

create table custumer (
id int primary key,
prenom varchar(50),
nom varchar(50)
);

insert into item (id, desk, price) values
(1, 'small desk', 100),
(2, 'large desk', 300),
(3, 'fan', 80);

insert into custumer (id, prenom, nom) values
(1, 'Greg', 'Jones'),
(2, 'Sandra', 'Jones'),
(3, 'Scott', 'Scott'),
(4, 'Trevor', 'Green'),
(5, 'Melanie', 'Johnson');

select * from item;

select * from item where price > 80;

select * from item where price < 300;

select * from custumer where nom = 'Smith';

select * from custumer where nom = 'Jones';

select * from custumer where prenom != 'Scott';