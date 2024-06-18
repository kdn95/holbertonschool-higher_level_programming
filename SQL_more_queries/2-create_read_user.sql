-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- creates the database hbtn_0d_2
-- If the database hbtn_0d_2 already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create user user_0d_2.
-- If the user user_0d_2 already exists, your script should not fail
-- The user_0d_2 password should be set to user_0d_2_pwd
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
GRANT SELECT on hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Apply changes
FLUSH PRIVILEGES;
