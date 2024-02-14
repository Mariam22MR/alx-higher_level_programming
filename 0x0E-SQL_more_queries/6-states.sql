-- Creates database that doesn't overwrite pre-existing versions
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use database
USE hbtn_0d_usa;
-- Creates a table
CREATE TABLE IF NOT EXISTS states(
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    UNIQUE(id)
);
