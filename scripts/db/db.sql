-- create databases
CREATE DATABASE nba_test;
CREATE DATABASE dummy; 

-- create dummy nbateams table 
CREATE TABLE IF NOT EXISTS dummy_teams (
  product_id INT NOT NULL,
  name varchar(250) NOT NULL,
  PRIMARY KEY (product_id)
);
