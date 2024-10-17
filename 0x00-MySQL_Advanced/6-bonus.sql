-- 
-- 
use test;
delimiter $$
create procedure AddBonus(user_id int, project_name varchar(255), score int)
begin
	select project_id into @project_id
	from projects where projects.project_name = project_name;
	update corrections set corrections.score = score 
	where corrections.user_id = user_id and corrections.project_id = @project_id;
end $$
delimiter;
