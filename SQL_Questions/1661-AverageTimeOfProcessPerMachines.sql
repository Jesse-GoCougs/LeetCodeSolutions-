SELECT 
    machine_id, 
    ROUND(AVG(endTime - startTime), 3) AS processing_time
FROM (
    SELECT
        machine_id, 
        process_id, 
        MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS startTime,
        MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS endTime
    FROM 
        Activity 
    GROUP BY
        machine_id, 
        process_id
) AS processTimes
GROUP BY 
    machine_id;