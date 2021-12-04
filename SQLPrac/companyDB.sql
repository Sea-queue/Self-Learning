USE Seaqueue_DB

-- drop table employee;
-- drop table branch;
-- drop table client;
-- drop table works_with;
-- drop table branch_supplier;

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    first_name VARCHAR(40),
    last_name VARCHAR(40),
    birth_day DATE,
    sex VARCHAR(1),
    salary INT,
    super_id INT,
    branch_id INT
);

CREATE TABLE branch (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(40),
    mgr_id INT,
    mgr_start_date DATE,
    FOREIGN KEY(mgr_id) REFERENCES employee(emp_id) ON DELETE SET NULL
);

ALTER TABLE employee
ADD FOREIGN KEY(branch_id)
REFERENCES branch(branch_id)
ON DELETE SET NULL;

ALTER TABLE employee
ADD FOREIGN KEY(super_id)
REFERENCES employee(emp_id)
ON DELETE SET NULL;

create table client (
    client_id INT PRIMARY KEY,
    client_name VARCHAR(40),
    branch_id INT,
    FOREIGN KEY(branch_id) REFERENCES branch(branch_id) ON DELETE SET NULL
);

create table works_with(
    emp_id INT,
    client_id INT,
    total_sales INT,
    PRIMARY KEY(emp_id, client_id),
    FOREIGN KEY(emp_id) REFERENCES employee(emp_id) on delete cascade,
    foreign key(client_id) references client(client_id) on delete cascade
);

create table branch_supplier(
    branch_id int,
    supplier_name varchar(40),
    supply_type varchar(40),
    primary key(branch_id, supplier_name),
    foreign key(branch_id) references branch(branch_id) on delete cascade
);

-- Corporate
insert into employee values(100, 'David', 'Wallace', '1967-11-17', 'M', 250000, NULL, NULL);
insert into branch values(1, 'Corporate', 100, '2006-02-09')
update employee set branch_id = 1 where emp_id = 100;
insert into employee values(101, 'Jan', 'Levinson', '1961-05-11', 'F', 110000, 100, 1);

-- Scranton
insert into employee values(102, 'Michael', 'Scott', '1964-03-15', 'M', 110000, 100, NULL);
insert into branch values(2, 'Scranton', 102, '1992-04-06');
update employee set branch_id = 2 where emp_id = 102;
insert into employee values(103, 'Angela', 'Martin', '1971-06-25', 'F', 63000, 102, 2);
insert into employee values(104, 'Kelly', 'Kapoor', '1980-02-05', 'F', 55000, 102, 2);
insert into employee values(105, 'Stanley', 'Hudson', '1958-02-19', 'M', 69000, 102, 2);

-- Stamford
insert into employee values(106, 'Josh', 'Porter', '1969-09-05', 'M', 78000, 100, NULL);
insert into branch values(3, 'Stamford', 106, '1998-02-13');
update employee set branch_id = 3 where emp_id = 106;
insert into employee values(107, 'Andy', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);
insert into employee values(108, 'Jim', 'Halpert', '1978-10-01', 'M', 71000, 106, 3);

-- Branch Supplier
insert into branch_supplier values(2, 'Hammer Mill', 'Paper');
insert into branch_supplier values(2, 'Uni-ball', 'Writing Utensils');
insert into branch_supplier values(3, 'Patriot Paper', 'Paper');
insert into branch_supplier values(2, 'J.T. Forms & Labels', 'Cutom Forms');
insert into branch_supplier values(3, 'Uni-ball', 'Writing Utensils');
insert into branch_supplier values(3, 'Hammer Mill', 'Paper');
insert into branch_supplier values(3, 'Stamford Lables', 'Custom Forms');

-- Client
insert into client values(400, 'Dunmore Highschool', 2);
insert into client values(401, 'Lackawana Country', 2);
insert into client values(402, 'FedEx', 3);
insert into client values(403, 'John Daly Law, LLC', 3);
insert into client values(404, 'Scranton Whitepages', 2);
insert into client values(405, 'Tiems Newspaper', 3);
insert into client values(406, 'FedEx', 2);

-- works with
insert into works_with values(105, 400, 55000);
insert into works_with values(102, 401, 267000);
insert into works_with values(108, 402, 22500);
insert into works_with values(107, 403, 5000);
insert into works_with values(108, 403, 12000);
insert into works_with values(105, 404, 33000);
insert into works_with values(107, 405, 26000);
insert into works_with values(102, 406, 15000);
insert into works_with values(105, 406, 130000);

SELECT * FROM employee;
SELECT * FROM branch;
SELECT * FROM branch_supplier;
select * from client;
select * from works_with;
