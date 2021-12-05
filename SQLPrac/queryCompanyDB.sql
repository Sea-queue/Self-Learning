USE Seaqueue_DB

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


-- Wild Card:
-- %: any number of characters
-- _: on character

-- find any client's who are an LLC
select * from client where client_name LIKE '%LLC';

-- find any branch suppliers who are in the label business
update branch_supplier
set supplier_name = 'Stamford Labels'
where supplier_name = 'Stamford Lables';
select * from branch_supplier;
select * from branch_supplier where supplier_name LIKE '%Labels';

-- find any employee born in October
update employee
set last_name = 'Bernard', birth_day = '1973-07-22', salary = 65000
where emp_id = 107;
select * from employee;
select * from employee where birth_day LIKE '____-10%';

-- find any clients who are schools
select * from client where client_name like '%school%';


-- Union:
-- both selects have to have the same number of columns

-- find a list of employee and branch name
select first_name from employee
union
select branch_name from branch;

-- list of employees / branch names / client names
select branch_name as Names from branch
union
select first_name from employee
union
select client_name from client;

-- find a list of all clients and branch_supplier_names
-- use the tablenName. to specify when column names are the same
select client_name, client.branch_id from client
union
select supplier_name, branch_supplier.branch_id from branch_supplier;

-- find a list of all money spent or earned by the company
-- when the values are the same, it prints only once
select salary from employee
union
select total_sales from works_with;


-- Joins
-- ------
insert into branch values(4, 'Buffalo', NULL, NULL);

-- find all branches and the names of their managers
select employee.emp_id, employee.first_name, branch.branch_name
from employee
join branch
on employee.emp_id = branch.mgr_id;

-- left join: include all the elements in employee table
select employee.emp_id, employee.first_name, branch.branch_name
from employee
left join branch
on employee.emp_id = branch.mgr_id;

-- right join: include all the elements in branch table
select employee.emp_id, employee.first_name, branch.branch_name
from employee
right join branch
on employee.emp_id = branch.mgr_id;

-- full join


-- Nested Query
-- get data from one table in order to inform the data from another table

-- find names of all employees who have sold over 30,000 to a single client
select employee.first_name, employee.last_name
from employee
where employee.emp_id IN (
    select works_with.emp_id
    from works_with
    where works_with.total_sales > 30000
);


-- find all clients who are handled by the branch that Micheal Scott manages
-- Assume you know Micheal's ID
select client.client_name
from client
where client.branch_id = (
    select branch.branch_id
    from branch
    where branch.mgr_id = 102
    limit 1
);


-- Delete
-- ------

-- on delete set null: when the foreign key gets deleted, set the key to null
delete from employee where emp_id = 102;
select * from branch;

-- on delete cascade: when the foreign key gets deleted, deleted the entire row
-- use this when the foreign key is part of the primary key
delete from branch where branch_id = 2;
select * from branch_supplier;


-- Trigger
-- -------
