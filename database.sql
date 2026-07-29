-- Creating a Students Table

CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    marks REAL
);

--Entering Simple Sample Data into Table

INSERT INTO students (id, name, age, course, marks)
VALUES
(101,'Darshan',20,'BCA',88.5),
(102,'Rahul',21,'BSc',76),
(103,'Priya',20,'BCom',91);