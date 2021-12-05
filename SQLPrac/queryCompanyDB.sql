-- find all employees ordered by salary most to least
select * from employee order by salary desc;

-- find all employees ordered by sex then name
select * from employee order by sex, first_name, last_name;

-- find first 5 employees in the table
select * from employee limit 5;

-- find the first and last names of all employees
select first_name, last_name from employee;

-- find the forename and surnames of all employees
select first_name as forename, last_name as surname from employee;

-- find all the different genders
select distinct sex from employee;

-- find all the different branch_id
select distinct branch_id from employee;


-- SQL Functions:
-- --------------

-- find the number of employees
select count(emp_id) from employee;

-- find the number of female employees born after 1970
select count(emp_id)
from employee
where sex = 'F' and birth_day > '1971-01-01';

-- find the average of all employee's salaries
select avg(salary) from employee;

-- find the male average salaries
select avg(salary) from employee where sex = 'M';

-- find the sum of all employee salaries
select sum(salary) from employee;

-- find how many males and females
select count(sex), sex
from employee
group by sex;

-- find the total sales of each salesman
select sum(total_sales), emp_id
from works_with
group by emp_id;

-- find how much each customer spend
select sum(total_sales), client_id
from works_with
group by client_id
order by sum(total_sales) desc;
