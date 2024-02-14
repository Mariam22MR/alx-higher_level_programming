-- Creates database that doesn't overwrite pre-existing versions
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use a database
USE hbtn_0d_usa;
-- Creates table with column that is foreign key
CREATE TABLE IF NOT EXISTS cities(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id),
    FOREIGN KEY(state_id) REFERENCES states(id));
