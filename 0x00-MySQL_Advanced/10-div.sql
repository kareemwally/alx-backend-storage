-- making a function to divide two params
-- the result is zero if b is zero
DELIMITER //

CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS float
DETERMINISTIC
BEGIN
    IF b = 0 THEN
        RETURN 0;
    ELSE
        RETURN a / b;
    END IF;
END //

DELIMITER ;
