-- making a procedure to apply bonus on a certain project
-- for a certain user
DELIMITER $$

CREATE PROCEDURE AddBonus(IN user_id INT, IN project_name VARCHAR(255), IN score INT)
BEGIN
    DECLARE project_id INT;

    -- Get project_id from the projects table
    SELECT id INTO project_id
    FROM projects
    WHERE name = project_name;

    -- If the project doesn't exist, insert it and retrieve the new project_id
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    -- Check if a correction already exists for the user and project
    IF EXISTS (SELECT 1 FROM corrections WHERE user_id = user_id AND project_id = project_id) THEN
        -- Update the correction score for this user and project
        UPDATE corrections
        SET score = score
        WHERE user_id = user_id AND project_id = project_id;
    ELSE
        -- Insert a new correction if it doesn't exist
        INSERT INTO corrections (user_id, project_id, score)
        VALUES (user_id, project_id, score);
    END IF;
    COMMIT;	
END $$

DELIMITER ;
