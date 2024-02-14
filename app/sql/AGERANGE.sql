ALTER TABLE users
ADD fasciaeta VARCHAR(20);

UPDATE users
SET fasciaeta =
	CASE
        WHEN Age < 18 THEN 'Under 18'
        WHEN Age < 24 THEN '18-24'
        WHEN Age < 35 THEN '25-34'
        WHEN Age < 45 THEN '34-44'
        WHEN Age < 55 THEN '45-54'
        ELSE 'over 55'
    END;



