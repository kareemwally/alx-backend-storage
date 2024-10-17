-- creating index on the table names
-- to speed up the search for large database
CREATE INDEX idx_name_first ON names ((LEFT(name, 1)));
