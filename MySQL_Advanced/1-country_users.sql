-- Create users table if it does not already exist
-- create enumeration of countries: US, CO and TN
-- -- Script can be executed on any database
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
    country ENUM('US', 'CO', 'TN') NOT NULL DEFAULT 'US'
);