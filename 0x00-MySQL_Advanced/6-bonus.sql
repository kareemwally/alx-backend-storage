-- 
-- 
use test;
delimiter $$
create procedure AddBonus(user_id int, project_name varchar(255), score int)
begin
	select project_id into @project_id
	from projects where projects.project_name = project_name;

	IF @project_id IS NULL THEN
        -- Insert the project into projects table if not found
        INSERT INTO projects (name) VALUES (project_name);
        -- Get the newly inserted project id
        SET @project_id = LAST_INSERT_ID();
	END IF;
	update corrections set corrections.score = score 
	where corrections.user_id = user_id and corrections.project_id = @project_id;
end $$
delimiter;
