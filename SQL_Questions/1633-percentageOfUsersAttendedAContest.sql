SELECT 
    r.contest_id, 
    ROUND(COUNT(*) / t.TotalUsers * 100, 2) AS percentage
FROM 
    Register AS r
JOIN 
(
    SELECT 
        COUNT(*) AS TotalUsers
    FROM 
        Users
) AS t
GROUP BY
    r.contest_id
ORDER BY 
    percentage DESC, 
    r.contest_id ASC;
