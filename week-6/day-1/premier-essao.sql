

--Create table finances (
--	id int primary key,
--	date date,
--	electricity float,
--	water float,
--	paid_by varchar(50)
--);

--insert into finances(id, date, electricity, water, paid_by) values
--(1,'2022-11-13',55.5 , 20.2, 'Yossi'),

--insert into finances(id, date, electricity, water, paid_by) values
--(2,'2022-11-13',57.1 , 20.2, 'Yossi'),
--(3,'2022-11-13',53.2 , 20.2, 'Lea'),
--(4,'2022-11-13',51.3 , 20.2, 'Annie'),
--(5,'2022-11-13',52.4 , 20.2, 'Bob');


--select * from finances;

--select date from finances;

--select water, paid_by from finances;

--select * from finances where id = 1;

--select date, paid_by from finances where id = 1;

--select * from finances where id != 2;

--select * from finances where id 1 or id = 2;

-- select * from finances where id in(1,2);

-- select max(water) from finances;

-- select min(electricity) from finances;

-- select avg(electricity) from finances where paid_by != ‘Bon’;

-- select paid_by, avg(water) from finances group by paid_by;

-- select paid_by, count(paid_by) from finances group by paid_by;

-- select sum(water), sum (electricity) from finances group by paid_by;

-- select sum(water) as water_sum, sum (electricity) as electricity_sum from finances group by paid_by;

select paid_by, sum(water + electricity) as total_sum from finances group by paid_by; 
