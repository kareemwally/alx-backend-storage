-- creating table users with
-- the fields/attributes id, email, name, country
CREATE TABLE IF NOT EXISTS users (
	id int NOT NULL AUTO_INCREMENT,
	email varchar(255) NOT NULL UNIQUE,
	name varchar(255),
	country enum('US','TN','CO') DEFAULT 'US' NOT NULL,
	PRIMARY KEY(id)
	);
