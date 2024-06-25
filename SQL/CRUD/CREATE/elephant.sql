-- students. name,email,mark,is_married

CREATE TABLE student(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(50),
    email VARCHAR(50),
    mark INTEGER,
    is_married BOOLEAN
)

-- INSERT INTO <table_name> (columnst) VALUES ()

-- INSERT INTO student
--  (name,email) 
--  VALUES
--  ('Benedict','ben@gmail.com')


-- INSERT INTO student 
-- (name,email,mark,is_married)
-- VALUES
-- ('John','sam@sam.com',34,FALSE)

-- REalistic
-- email are unique
-- don't have email address
-- Garbage Data.

INSERT INTO student
(name,email)
VALUES
('Samuel','sammambu@gmail.com')

