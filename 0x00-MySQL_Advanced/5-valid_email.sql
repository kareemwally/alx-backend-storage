-- resetting the mail-status
-- whenever the email is updated
DELIMITER $$

CREATE TRIGGER email_toggle
AFTER UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END $$

DELIMITER ;
