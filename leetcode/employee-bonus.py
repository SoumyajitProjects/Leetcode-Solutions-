# Write your MySQL query statement below
SELECT name, bonus 
FROM Employee LEFT JOIN Bonus on Employee.empID = Bonus.empID
WHERE bonus < 1000 or bonus is NULL