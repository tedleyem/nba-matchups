# Postgres commands and helpful resources 

#### create user with password and permissions
CREATE ROLE user_name PASSWORD 'PaSSwOrD' NOSUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;

Grant Privileges to the User

By default, new users do not have any privileges except for login. To add privileges when creating a user, run the createuser client utility in the following format:

createuser <option> <name>

To do the same in PSQL, run:

CREATE USER <name> WITH <option>;

Below is a table with commonly used options for both methods.
Option Syntax	PSQL	Explanation
-s
--superuser	SUPERUSER	Add the superuser privilege.
-S
--no-superuser	NOSUPERUSER	No superuser privilege (default).
-d
--createdb	CREATEDB	Allows the user to create databases.
-D
--no-createdb	NOCREATEDB	Not allowed to create databases (default).
-r
--createrole	CREATEROLE	Allows the user to make new roles.
-R
--no-createrole	NOCREATEROLE	Not allowed to create roles (default).
-i
--inherit	INHERIT	Automatically inherit the privileges of roles (default).
-I
--no-inherit	NOINHERIT	Do not inherit privileges of roles.
-l
--login	LOGIN	Allows the user to log into a session with the role name (default).
-L
--no-login	NOLOGIN	Not allowed to log into a session with the role name.
--replication	REPLICATION	Allows initiating streaming replication and activating/deactivating backup mode.
--no-replication	NOREPLICATION	Not allowed to initiate streaming replication or backup mode (default).
-P
--pwprompt	PASSWORD '<password>'	Initiates password creation prompt or adds provided password to the user. Avoid using this option to create a passwordless user.
/	PASSWORD NULL	Specifically sets the password to null. Every password authentication fails for this user.
-c <number>
--connection-limit=<number>	CONNECTION LIMIT <number>	Sets the maximum number of connections for user. Default is without limit.


# LINKS 

# dummy data 
https://levelup.gitconnected.com/creating-and-filling-a-postgres-db-with-docker-compose-e1607f6f882f

