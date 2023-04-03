--Write an SQL query to report the patient_id, patient_name and conditions of the patients who have Type I Diabetes.
--Type I Diabetes always starts with DIAB1 prefix.
--Return the result table in any order.
--The query result format is in the following example.

--Example:
--Input:                                              Output:
--Patients table:
--+------------+--------------+--------------+        +------------+--------------+--------------+
--| patient_id | patient_name | conditions   |        | patient_id | patient_name | conditions   |
--+------------+--------------+--------------+        +------------+--------------+--------------+
--| 1          | Daniel       | YFEV COUGH   |        | 3          | Bob          | DIAB100 MYOP |
--| 2          | Alice        |              |        | 4          | George       | ACNE DIAB100 |
--| 3          | Bob          | DIAB100 MYOP |        +------------+--------------+--------------+
--| 4          | George       | ACNE DIAB100 |
--| 5          | Alain        | DIAB201      |
--+------------+--------------+--------------+

--Explanation: Bob and George both have a condition that starts with DIAB1.


SELECT * FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
