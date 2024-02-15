-- lists number of records with same score in table second_table in MySQL server.
-- Records ordered by descending.
SELECT `score`, COUNT(*) AS `number` FROM `second_table` GROUP BY `score` ORDER BY `number` DESC;
