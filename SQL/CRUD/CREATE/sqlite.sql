-- CREATE TABLE student(
--     id INTEGER PRIMARY KEY AUTOINCREMENT,
--     name TEXT NOT NULL CHECK(LENGTH(name) > 4),
--     email TEXT NOT NULL UNIQUE CHECK(LENGTH(email) > 4),
--     mark INTEGER NOT NULL DEFAULT 0 CHECK(mark > -1 AND mark < 101),
--     is_married BOOLEAN NOT NULL DEFAULT 0
-- );
INSERT INTO student 
(name, email, mark,is_married)
 VALUES
('Samuel', 'samuel@gmail.com',23,1),
('John M', 'John@gmail.com',90,0)


