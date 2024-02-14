-- Creates table with constraint on column to have unique value
-- for each row, which is never empty when value isn't given
CREATE TABLE IF NOT EXISTS unique_id(
	id INT DEFAULT 1,
	name VARCHAR(256),
	UNIQUE(id)
);
