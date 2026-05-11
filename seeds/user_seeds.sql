TRUNCATE TABLE users RESTART IDENTITY CASCADE;

INSERT INTO users (username, password) VALUES ('testuser', 'testpassword');