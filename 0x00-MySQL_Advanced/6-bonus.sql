-- making a procedure to apply bonus on a certain project
-- for a certain user
DELIMITER //

CREATE PROCEDURE AddBonus(
    IN p_user_id INT,
    IN p_project_name VARCHAR(255),
    IN p_score INT
)
BEGIN
    DECLARE v_project_id INT;

    -- Start transaction
    START TRANSACTION;

    -- Check if the project exists
    SELECT id INTO v_project_id
    FROM projects
    WHERE name = p_project_name;

    -- If project doesn't exist, create it
    IF v_project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (p_project_name);
        SET v_project_id = LAST_INSERT_ID();
    END IF;

    -- Add the correction
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (p_user_id, v_project_id, p_score);

    -- Commit the transaction
    COMMIT;
END //

DELIMITER ;
