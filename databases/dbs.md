# Databases

## 0) what is a database?

why do we need databases?

let's think about microservices architecture:
each service need to have a way to store data, but they all need to share the data

we'll use one extra server that will store the data, and this is a database

we'll also seperate this way the information and the code logic

the persistency is the ability to store data after the program is closed





## 1) kinds of databases

2 main types of databases:
- relational
- non-relational

relational databases: (like relationships)
- use structured query language (SQL / tables with rows and columns)
- use tables to store data
- use rows to store data
- use columns to store data

let's take a student as an example:
we can create a table for the students:
- id, name, age, gender, address, phone

if we want to add a new student, we need to add a new row to the table, also if we want to give one of the students a new phone number, we need to update the table, which means for all the students we need to update the phone number - tables are not flexible

the studends also learn different subjects, so we can create a table for the subjects:
- id, name_of_subject, description

how can i link the students to the subjects?
this is where the relationships come in
there are 3 types of relationships:
let's take one of them
one more one (one student can learn one subject):
this is a new table:
- student_id, subject_id, enrollment_date, grade


non-relational databases:
- those are more like json files, more flexible than relational databases
- use unstructured query language (NoSQL)
- use key-value pairs to store data
- use documents to store data
- use graphs to store data

this has pro and cons:
pros: more flexible, more scalable, more performance
cons: less structured, less data integrity, less data consistency

let's take again the student relationships:
in non-relational databases the student courses will look like this:
```json
{
    "student_id": "1",
    "courses": [
        "course_id": "1",
        "enrollment_date": "2021-01-01",
        "grade": "A"
    ]
}
```

so if we want to change name of one course for all the students:
in relational databases we need to update the couses name in the table, 
but in non-relational databases we can just change the name of the course in the array

both of those databases have their own pros and cons, and they are used in different cases


## 2) relational databases

here's a few examples of relational databases:
- MySQL
- PostgreSQL
- Oracle
- Microsoft SQL Server

in all those dbs techs, we'll use the same language to interact with the db:
- SQL (Structured Query Language)

there are little differences in the syntax, but the logic is the same

we'll focus more on PostgreSQL, it's a very popular db

btw, the opposite of sql is no sql, and the opposite of relational is non-relational


## 3) download and run PostgreSQL
we'll download the image of the postgres db:
```bash
docker pull postgres 
```
we don't have to pull the image, on the run command it'll pull the image automatically

then we'll run the container:
```bash
docker run --name first-postgres -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword -e POSTGRES_DB=mydb -d -p 5432:5432 postgres
```

## 4) how to interact with the db

the db run on the server, and we need to connect to it as clients
the best tool to interact with the db is called sqlectron


## 5) create db and tables

we'll use the psql command to interact with the db

create db:
```sql
CREATE DATABASE college;

to connect to the db:
\c college

create table:
CREATE TABLE students (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    email VARCHAR(100) NOT NULL
);
```
to view the tables in the db:
\dt

to view the data:
```sql
SELECT * FROM students;
```


```sql
# to select specific tables and columns
SELECT name, age FROM students LIMIT 3;
```

to insert data:
```sql
INSERT INTO students (name, age, email) VALUES ('John Doe', 25, 'john.doe@example.com');
```

to update data:
```sql
UPDATE students SET age = 26 WHERE name = 'John Doe';
```

to update 1 cell:
```sql
UPDATE students SET age = 26 WHERE name = 'John Doe';
```

to update all the columns to a row number:
```sql
UPDATE students SET age = 26, email = 'john.doe@example.com' WHERE id = 1;
```

to delete data:
```sql
DELETE FROM students WHERE id = 1;
```

command to insert 5 rows at once:
```sql
INSERT INTO students (name, age, email) VALUES ('John Doe', 25, 'john.doe@example.com'), ('Jane Smith', 26, 'jane.smith@example.com'), ('Jim Beam', 27, 'jim.beam@example.com'), ('Jill Johnson', 28, 'jill.johnson@example.com'), ('Jack Daniels', 29, 'jack.daniels@example.com');
```

SELECT and sort:
```sql
SELECT * FROM students ORDER BY age DESC;
```

or:
```sql
SELECT * FROM students ORDER BY age ASC;
```

commit:
```sql
COMMIT;
```


to delete rows:
```sql
DELETE FROM students WHERE id = 1;
```

# to delete all the rows:
```sql
DELETE FROM students;
```

to delete the table:
```sql
DROP TABLE students;
```


## 6) crud operations (create, read, update, delete)

create:
```sql
INSERT INTO students (name, age, email) VALUES ('John Doe', 25, 'john.doe@example.com');
```

read:
```sql
SELECT * FROM students;
```

update:
```sql
UPDATE students SET age = 26 WHERE name = 'John Doe';
```


more examples:
```sql
UPDATE students
SET email = 'updated_' || email
WHERE id = 1;
```
this will update the email of the student with the id 1 to updated_email@example.com

delete:
```sql
DELETE FROM students WHERE id = 1;
```

F.P.S - Filter Pagination Sorting 
- filter: works with WHERE: 
```sql
SELECT * FROM students WHERE age > 25;
```

more examples:
```sql
SELECT * FROM students WHERE name LIKE 'Jo%';
this will return all the students that have the name starting with Jo
```

```sql
SELECT * FROM students WHERE name LIKE 'Jo%' or age > 25;
this will return all the students that have the name starting with Jo or are older than 25
```

```sql
SELECT * FROM students WHERE id <= 5;
this will return all the students that have the id less than or equal to 5
```

- pagination: works with LIMIT and OFFSET (בעברית עימוד, כמו לתת למישהו רק עמוד אחד מתוך ספר)
```sql
SELECT * FROM students LIMIT 3 OFFSET 2;
```

- sort: works with ORDER BY
```sql
SELECT * FROM students ORDER BY age DESC;
```


## 7) Crud operations part 2

## 8) get value back on command when creating

we're going to use another sofware, becuase elctron is not the best for this:
- DBeaver
    
to connect to the db:
create new connection with the plug icon
right click on the db and click on open sql editor

to change the setting so it'll display the code in uppercase:
- file > properties > sql editor > global settings > sql editor > code editor > convert to uppercase

to return the value back on command when creating:
```sql
INSERT INTO students (name, age, email) VALUES ('test', 20, 'test@gmail.com') 
RETURNING id;
```

i can also return json representation with row_to_json:
```sql
INSERT INTO students (name, age, email) VALUES ('test', 20, 'test@gmail.com') 
RETURNING row_to_json(students);
```

## 10) Aggregation and grouping

first what's the difference between aggregation and grouping?
aggregation is when we want to get a single value based on a condition, example:
```sql
SELECT COUNT(*) FROM students WHERE age > 25;
this will return the number of students that are older than 25

avg and sum are also aggregation functions:
```sql
SELECT AVG(age) FROM students;
SELECT SUM(age) FROM students;
```

grouping is when we want to get multiple values from a table
for example:
```sql
SELECT COUNT(*) FROM students GROUP BY age;
```
this will return the number of students for each age

it's possible to use multiple functions at once:
```sql
SELECT COUNT(*) as total_count, 
AVG(age) as avg_age,
SUM(age) as sum_age,
MIN(age) as min_age,
MAX(age) as max_age
FROM students;
```

## 11) Grouping 
```sql
SELECT age, COUNT(*) as count FROM students
GROUP BY age
ORDER BY count ASC;
```
this expression will return the number of students for each age and order them by the number of students in ascending order
