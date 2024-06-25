-- One student has many parents (2)
-- One Parent has many students (2)

-- DROP TABLE IF EXISTS student,parent;


-- CREATE TABLE parent(
--     id BIGSERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );


-- CREATE TABLE student(
--     id BIGSERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL
-- );

-- COMBINED KEY

-- CREATE TABLE parent_student(
--     id BIGSERIAL PRIMARY KEY,
--     parent_id BIGINT NOT NULL REFERENCES parent(id),
--     student_id BIGINT NOT NULL REFERENCES student(id),
--     UNIQUE(parent_id,student_id)
-- )

-- INSERT INTO parent 
-- (name)
-- VALUES
-- ('pa'),
-- ('pb'),
-- ('pc'),
-- ('pd');


-- INSERT INTO student
-- (name)
-- VALUES
-- ('st1'),
-- ('st2'),
-- ('st3'),
-- ('st4'),
-- ('st5')

-- SELECT * FROM parent_student
-- WHERE student_id=5

-- SELECT 
--     p.name AS parent_name,
--     p.id AS parent_id,
--     s.name AS student_name,
--     s.id AS student_id
-- FROM
--     parent_student AS ps
-- INNER JOIN
--     parent AS p ON ps.parent_id = p.id
-- INNER JOIN
--     student AS s ON ps.student_id = s.id;

SELECT 
    p.name AS cats_dogs,
    p.id AS parent_id,
    s.name AS student_name,
    s.id AS student_id
FROM
    parent AS p
INNER JOIN
    parent_student AS ps ON ps.parent_id = p.id
INNER JOIN
    student AS s ON ps.student_id = s.id;
