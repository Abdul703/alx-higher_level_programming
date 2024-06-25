-- script that creates the database hbtn_0d_usa and the table state

-- creating database
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- creating state table
CREATE TABLE IF NOT EXISTS states(
    id INT PRIMARY KEY DEFAULT 1,
    name VARCHAR(256) NOT NULL
);
