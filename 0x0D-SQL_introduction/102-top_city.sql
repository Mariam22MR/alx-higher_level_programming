-- Computes and filters average of a group of records
-- In table in databasec.
SELECT city, AVG(value) AS avg_temp FROM temperatures
    WHERE month = 7 OR month = 8
    GROUP BY city
    ORDER BY avg_temp DESC
    LIMIT 3;
