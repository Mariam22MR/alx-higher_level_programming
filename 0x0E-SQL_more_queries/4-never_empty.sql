-- Creates table with constraint on column and another
-- column that is never empty when given NULL value
CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
