USE Seaqueue_DB

-- DROP TABLE student;      -- delete the table

CREATE TABLE student (
    student_id INT AUTO_INCREMENT,
    name VARCHAR(20) NOT NULL,
    major VARCHAR(20) DEFAULT 'undecided',
    PRIMARY KEY(student_id)
);

DESCRIBE student;           -- show table, column types     
SELECT * FROM student;      -- show all the elements

ALTER TABLE student ADD gpa DECIMAL(3, 2);
ALTER TABLE student DROP COLUMN gpa;

INSERT INTO student VALUES(1, 'Seaqueue', 'CS');
INSERT INTO(name, major) VALUES('Gina', 'Business');

UPDATE student SET major = 'Bio' WHERE major = 'Business';
update student set name = 'Tom' where name = 'Briany';
-- change everyone's major to 'undecided':
update student set major = 'undecided';

delete from student where student_id = 5;
delete from student where name = 'Briany';
-- delete everyone:
delete from student;

select * from student;
select name from student;
select student_id from student;
select major from student;
select student.name from student order by name;
select student.name from student order by name desc;
select * from student limit 1;
select * from student where major = 'CS';
select name from student where major = 'CS' or major = 'Business';
select * from student where major in ('CS', 'Business');
select * from student where major in ('CS', 'Business') and student_id > 3;

-- comparison: < , >, = , <=, >=, <>(not equal), AND, OR
select * from student  where name <= 'Diego' AND major = 'Business';
