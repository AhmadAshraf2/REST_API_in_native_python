CREATE TABLE categories(ID INT PRIMARY KEY NOT NULL, category VARCHAR(20) NOT NULL UNIQUE);
INSERT INTO categories(ID, category) VALUES (1, 'entertainment'), (2, 'technology');