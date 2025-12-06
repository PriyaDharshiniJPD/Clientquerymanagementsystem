DROP TABLE IF EXISTS queries;

CREATE TABLE queries (
    query_id SERIAL PRIMARY KEY,
    mail_id VARCHAR(100) NOT NULL,
    mobile_number VARCHAR(20) NOT NULL,
    query_heading TEXT NOT NULL,
    query_description TEXT NOT NULL,
    status VARCHAR(10) NOT NULL,
    query_created_time TIMESTAMP NOT NULL,
    query_closed_time TIMESTAMP
);
SELECT * FROM queries