-- Different types of columns
-- Data type you want to store.
-- Differes from different data-bases.

create table student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    marks INTEGER,
    adm_no INTEGER,
    is_married INTEGER, 
    bank_balance REAL
)