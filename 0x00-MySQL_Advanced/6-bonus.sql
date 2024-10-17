-- making a procedure to apply bonus on a certain project
-- for a certain user
DELIMITER $$

CREATE PROCEDURE AddBonus(user_id INT, project_name VARCHAR(255), score INT)
BEGIN
    DECLARE project_id INT;

    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    IF EXISTS (SELECT 1 FROM corrections WHERE user_id = user_id AND project_id = project_id) THEN
        UPDATE corrections
        SET score = score
        WHERE user_id = user_id AND project_id = project_id;
    ELSE
        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, project_id, score);
    END IF;
END $$

DELIMITER ;
