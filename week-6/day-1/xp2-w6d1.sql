-- create table students (
-- id int primary key,
-- last_name varchar(50),
-- first_name varchar(50),
-- birth_date date
-- );


-- insert into students (id, last_name, first_name, birth_date) values
-- (1, 'Marc', 'Benichou', '1998-11-02'),
-- (2, 'Yoan', 'Cohen', '2010-12-03'),
-- (3, 'Lea', 'Benichou', '1987-07-27'),
-- (4, 'Amelia', 'Dux', '1996-04-07'),
-- (5, 'David', 'Grez', '2003-06-14'),
-- (6, 'Omer', 'Simpson', '1980-10-03');

-- select * from students;

-- select last_name, first_name from students;

-- select id =2 from students;

-- select first_name = 'Benichou', last_name = 'Marc' from students;

-- select first_name from students where first_name like '%a%';

-- select last_name from students where last_name like '%A%';

-- select last_name from students where last_name like '%a';

-- select last_name FROM students WHERE last_name LIKE '_o%';

-- select * from students where id in(1,3);

select * from students where birth_date < '2000-01-01';

