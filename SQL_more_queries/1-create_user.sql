-- Create user user_0d_1
-- ps = user_0d_1_pwd
-- if already exists, script shouldn't fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- Provide all privileges
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
-- Apply changes
FLUSH PRIVILEGES;
