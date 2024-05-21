-- shows a lists of all records of the table 'second_table' of the database hbtn_0c_0 in MySQL server.
-- display both the score and the name - in this order
-- Records ordered by score - top first
SELECT `score`, `name`
FROM `second_table`
ORDER BY `score` DESC;
