create table student(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(250),
    email VARCHAR(250),
    marks INTEGER,
    dob DATE,
    adm_no BIGINT,
    is_married BOOLEAN, 
    json_data JSON,
    bank_balance REAL
)