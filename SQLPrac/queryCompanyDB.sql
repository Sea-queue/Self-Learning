-- find all employees ordered by salary most to least
select * from employee order by salary desc;

-- find all employees ordered by sex then name
select * from employee order by sex, first_name, last_name;
