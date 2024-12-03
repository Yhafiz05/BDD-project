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