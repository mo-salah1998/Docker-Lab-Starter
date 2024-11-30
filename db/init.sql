CREATE DATABASE taskdb;
use taskdb;

CREATE TABLE tasks (
  name VARCHAR(20) PRIMARY KEY
); 

INSERT INTO tasks
  (name)
VALUES
  ('yousri'),
  ('ayoub');