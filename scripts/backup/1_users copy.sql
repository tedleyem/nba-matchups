-- create roles with permissions
CREATE ROLE viewer;
CREATE ROLE editor;
CREATE ROLE admin;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO viewer;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO viewer;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT,INSERT,UPDATE ON TABLES TO editor;

-- create admin user 
CREATE USER admin WITH SUPERUSER PASSWORD 'password';

-- create user ted for basic user access  
CREATE ROLE ted CREATEDB CREATEROLE WITH LOGIN ted PASSWORD 'reverse';
GRANT editor TO ted;

-- create guest user 
CREATE ROLE guest WITH LOGIN guest PASSWORD 'guest';
GRANT viewer TO guest;
-- create user roz 
CREATE ROLE roz CREATEDB CREATEROLE WITH LOGIN roz PASSWORD 'diamonds';
GRANT viewer TO roz;