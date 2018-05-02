CREATE TABLE blogs(ID INT PRIMARY KEY NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL, category varchar(20) REFERENCES categories(category));
