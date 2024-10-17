-- 
create function SafeDiv(IN a int, IN b int) return int
begin
	declare res int;
	if b = 0 then
		return 0;
	else
		return a/b;
