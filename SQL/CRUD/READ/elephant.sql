
-- SELECT <what column or columns> FROM <TABLE> WHERE
--

-- SELECT name,email
-- FROM student

--wildcard. *<ALL>

-- SELECT * FROM 
-- student

-- Where

-- SELECT * 
-- FROM student
-- WHERE name='Samuel'

-- SELECT * 
-- FROM student
-- WHERE mark>40 and mark<60


-- Aggregrate queries

-- make a qury to get the total number
-- of students who have below 40

-- SELECT COUNT(*)
-- FROM student
-- WHERE mark>50

-- SUM


SELECT SUM(mark)
FROM student

-- AVG 

-- MAX

-- MIN