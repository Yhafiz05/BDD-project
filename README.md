# Evaluating the time performance of postgresql and monetdb

## Prerequisites
1. Have started a postgres database
2. Have started a monetdb database
3. Having at least python 3.8

## Clone this repository
```
git clone https://github.com/Yhafiz05/BDD-project.git
```
## Creating a table in your database

1. Postgresql

```
psql -U <your_user> -d <your_database> -f ./podcast_rankings.sql
```

2. Monetdb

```
mclient -u <username> -d <database> -i ./podcast_rankings.sql
```
## Insertion of data

we inserted our data directly via the datagrip code editor, which lets you load a table directly from a csv file.
You may need to configure a jdbc driver for monetdb. You can find it via this link : https://www.monetdb.org/documentation-Aug2024/user-guide/client-interfaces/libraries-drivers/jdbc-driver/.

![data](data/Capture%20d’écran%202024-12-03%20à%2012.30.26%E2%80%AFPM.png)