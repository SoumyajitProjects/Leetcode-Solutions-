# Write your MySQL query statement below
SELECT name FROM Employee WHERE Id IN (SELECT ManagerId FROM Employee GROUP BY ManagerID
HAVING (COUNT(DISTINCT Id)) >= 5)