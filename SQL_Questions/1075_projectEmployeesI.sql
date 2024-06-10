SELECT p.project_id, ROUND(AVG(e.experience_years), 2) AS average_years
FROM Project as p left join Employee AS e
ON e.employee_id 