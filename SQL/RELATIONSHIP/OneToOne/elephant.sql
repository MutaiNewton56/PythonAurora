
-- DROP TABLE student,parent

-- CREATE TABLE parent(
--     id BIGSERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     email VARCHAR(255) NOT NULL UNIQUE
-- );

-- -- REFERENCES.
-- -- SQLITE FK

-- CREATE TABLE student
-- (
--     id BIGSERIAL PRIMARY KEY,
--     name VARCHAR(255) NOT NULL,
--     parent_id BIGINT NOT NULL UNIQUE REFERENCES parent(id) ON DELETE 
--     CASCADE
-- )

-- INSERT INTO parent
-- (name,email)
-- VALUES
-- ('Parent A','parenta@example.com'),
-- ('Parent B','parentb@example.com'),
-- ('Parent C','parentc@example.com')

-- INSERT INTO student
-- (name,parent_id)
-- VALUES
-- ('student1',1)