# LOGS ANALYSIS TOOL

a tiny python tool to analyze data in the "news" database and display coressponding reports

### Description

the code is divided into 3 functions get_pop_art, get_pop_auth and get_err_days

the function "get_pop_art" is responsible for displaying the top 3 most popular articles
the articles are displayed with the total number of views in descending order.

the function "get_pop_auth" is responsible for displaying the popular authors.
it will display each author with the total number of views for his/her articles in the form of a list ordered descendingly.

he function "get_err_days" is responsible for displaying the days with bad HTTP  requests that exceeded 1% of the total requests for that day.


### Details

the function "get_pop_art" is responsible for displaying the top 3 most popular articles
the articles are displayed with the total number of views in descending order.

the number of views is obtained by counting the number of successful requests to the article page which is found in the server log
the sql statement will count every successful request to a path containing the article slug(while this is not the most accurate way as there are requests for just refreshing the page so there will be error factor which can be calculated by counting requests from the same IP  at a narrow time period for example during the same hour of the day) then it will sort the result descendingly displaying the top 3 records.

the function "get_pop_auth" is responsible for displaying the popular authors.
it will display each author with the total number of views for his/her articles in the form of a list ordered descendingly.
the fuction will count each successful request to an article while connecting the log to the authors through the articles table,hence, summing up all views of all articles for each author.
here also we count a successful request by having "200 OK" response

the function "get_err_days" is responsible for displaying the days with bad HTTP  requests that exceeded 1% of the total requests for that day.
to accomplish this we started by creating two views 1- the bad_req view which is created by the command "create view bad_req as select date(log.time) as Date ,count(status)as bad_req from log where log.status<>'200 OK' group by date(log.time) ;" and it will count all the bad HTTP requests for each day(any request with response not "200 OK"). 2- the tot_req view which is created by the command "create view total_req as select date(log.time) as Date ,count(status)as total_req from log  group by date(log.time) ;" and it will count the total requests for each day.
by having the bad requests and the total requests we calculate the percentage then filter by allowing only percentage greater than 1%.


### Prerequisites

python 3.7.1 and 
the "news" database should be set and populated on postgreSQL database system
there are two views to be created before starting the reporting tool the "bad_req"
and "total_req" views(see installation section)

```
creat view ....
```

### Installing

** installing python 3

please visit the link provided below in the "built with" section and follow the instruction 
to install python 3 on your system.

** installing postgreSQL

please visit the link provided below in the "built with" section and follow the instruction 
to install postgreSQL on your system.

** setting the "News" database
first you have to create the "news" database by running the following commands
log in to the postgre database system (you must have enough privileges for your account)
```
psql
```
then run the create database command

```
create database news;

```

then Download the data

Next, download the data [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). You will need to unzip this file after downloading it. The file inside is called newsdata.sql.
To run the reporting tool, you'll need to load the site's data into your local database. 
To load the data, cd into the downloaded file directory and use the command
```
 psql -d news -f newsdata.sql

```

Here's what this command does:

    psql — the PostgreSQL command line program
    -d news — connect to the database named news which has been created in the last step
    -f newsdata.sql — run the SQL statements in the file newsdata.sql

Running this command will connect to your installed database server and execute the SQL commands in the downloaded file, creating tables and populating them with data. 

** creating required views
in order for this reporting tool to work succefully please create the required views 
as follow ...

```
create view bad_req as select date(log.time) as Date ,count(status)as bad_req from log where log.status<>'200 OK' group by date(log.time) ;
```

second view

```
create view total_req as select date(log.time) as Date ,count(status)as total_req from log  group by date(log.time) ;
```
alternatively you can import the file "createviews.sql" directly to the database by running the command :

```
 psql -d news -f createviews.sql

```

where the previous create view command will be executed automaticly

## Running the tool

just type "python log_analysis.py" at the open terminal to run the reporting tool



```
python log_analysis.py
```

### Sample output
![](https://github.com/drmtm/logs_analysis/blob/master/Screenshot.png)

## Built With

* [Python](https://www.python.org/) - The programing language used
* [PostgreSQL](https://www.postgresql.org/) - the Database system



## Authors

* **Mohammed Aly** - *Initial work* - [DrMtM](https://github.com/drmtm)



## Acknowledgments

* my mentors at udacity full stack web developer nano degree
