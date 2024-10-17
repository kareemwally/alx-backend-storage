-- triggers are crucial part of tracking evets in MYSQl 
-- and need a delimiter to write it properly
delimiter //
create trigger new_trigger AFTER INSERT ON orders FOR each row
BEGIN 
update items set quantity = quantity - New.number WHERE items.name = New.item_name;
END;
//
delimiter;
