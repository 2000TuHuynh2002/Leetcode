# Write your MySQL query statement below

SELECT E1.name
FROM Employee E1, (SELECT managerId
					FROM Employee
					GROUP BY managerId
					HAVING COUNT(managerId)>=5) E2
WHERE E1.id=E2.managerId
