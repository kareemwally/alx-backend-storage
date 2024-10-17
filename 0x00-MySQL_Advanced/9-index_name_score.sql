-- creating an index for 2 columns
-- the 1st char of name field and score field
CREATE INDEX idx_name_first_score ON names (name(1), score);
