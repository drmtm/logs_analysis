#!/usr/bin/env python3
# Solution for the first project "Logs Analysis"!

import psycopg2

DBNAME = "news"
db = None
c = None


def db_connect():
    """Sets the dtabase and  cursor objects if connectd successfully"""
    global db
    global c
    try:
        db = psycopg2.connect(database=DBNAME)  # connecting to the database
        c = db.cursor()
    except psycopg2.DatabaseError as e:
        print("ERROR CONNECTING TO THE DATABASE\n ERROR:({}) ".format(e))
        return(1)

    return None  # used later to test for errors


def db_close():
    """close the connection to database and clear cursor object """
    global db
    global c
    try:
        c = None
        db.close()  # closing connection  to the database

    except psycopg2.DatabaseError as e:
        print("""ERROR  CLOSING CONNECTION TO
        THE DATABASE\n ERROR:({}) """.format(e))
        return(1)

    return None  # used later to test for errors


def get_pop_art():
    """Return the 3 top most articles regarding views"""
    global c
    sql_str = """select articles.title as Article ,count(log.path) as Views
         from articles,log where log.path like '%'|| articles.slug||
         '%' and log.status='200 OK' group by articles.title
         order by Views desc limit 3;"""
    c.execute(sql_str)
    sql_result = c.fetchall()
    print("The most popular three articles of all time :\n")
    for art in sql_result:
        print("   {}  -  {}  views".format(art[0], art[1]))
    print("-" * 70)
    print("\n")

    return None  # may be used later to test for errors


def get_pop_auth():
    """Add a post to the 'database' with the current timestamp."""
    global c
    sql_str = """select authors.name as Author ,count(log.path) as Views from
         authors,articles,log where authors.id=articles.author
         and log.path like '%'|| articles.slug|| '%' and log.
        status='200 OK' group by authors.name order
         by Views desc ;"""
    c.execute(sql_str)
    sql_result = c.fetchall()
    print("The  most popular article authors of all time :\n")
    for aut, count in sql_result:
        print("   {}  -  {}  views".format(aut, count))
    print("-" * 70)
    print("\n")

    return None


def get_err_days():
    """Return all days with error in requests that exceed 1% of the total
    requests  considering all none "200 OK" as errors(n.b this is not so
    accurate but it will do the job) """
    global c
    sql_str = """select to_char(total_req.date,'month dd,yyyy') as Date,((100
         *bad_req.bad_req::float / total_req.total_req)::numeric
        (2,1)) as error_percent from bad_req join total_req
         on bad_req.date=total_req.date where (100 * bad_req.bad_req
         / total_req.total_req) > 1;"""
    c.execute(sql_str)
    sql_result = c.fetchall()
    print("The  day(", "s) with  more than 1% of requests lead to errors :\n")
    for day, percent in sql_result:
        print("   {}  -  {}  % errors".format(day, percent))
    print("-" * 70)
    print("\n")

    return None


if __name__ == '__main__':
    reports = [db_connect, get_pop_art, get_pop_auth, get_err_days, db_close]
    print("\n\n		PROJECT: LOG ANALYSIS\n\n")
    print("	a tool to analyze data in news database and display reports\n")
    print("-" * 70)
    print("\n")
    for report in reports:
        ret_val = report()
        if ret_val == 1:
            print("*********EXIT WITH ERROR***********")
            break
    if ret_val != 1:
        print("***********END OF REPORTS************ ")
