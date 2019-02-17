# LOGS ANALYSIS TOOL

a tiny python tool to analyze data in the "news" database and display coressponding reports

### Description

the code is divided into 3 functions get_pop_art, get_pop_auth and get_err_days

the function "get_pop_art" is responsible for displaying the top 3 most popular articles
by counting the number of successful requests to the article page which is found in the server log
the sql statement will count every successful request to a path containing the article slug(while this is not the most accurate way as there are requests for just refreshing the page so there will be error factor which can be calculated by counting requests from the same IP  at a narrow time period for example during the same hour of the day) then it will sort the result descendingly displaying the top 3 records.

the function "get_pop_auth" 


### Prerequisites

python 3.7.1
the "news" database should be set and populated on postgreSQL database system
there are two views to be created before starting the reporting tool the "bad_req"
and "total_req" views(see installation)

```
creat view ....
```

### Installing

in order for this reporting tool to work succefully please create the required views 
as follow ...

```
create view bad_req as select date(log.time) as Date ,count(status)as bad_req from log where log.status<>'200 OK' group by date(log.time) ;
```

second view

```
create view total_req as select date(log.time) as Date ,count(status)as total_req from log  group by date(log.time) ;
```


## Running the tool

just type "python log_analysis.py" at the open terminal to run the reporting tool



```
python log_analysis.py
```



## Built With

* [Python](https://www.python.org/) - The programing language used
* [PostgreSQL](https://www.postgresql.org/) - the Database system



## Authors

* **Mohammed Aly** - *Initial work* - 



## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc

