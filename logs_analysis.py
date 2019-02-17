# Solution for the first project "Logs Analysis"!

import psycopg2

DBNAME = "news"


def get_pop_art():
    """Return the 3 top most articles regarding views"""
    db = psycopg2.connect(database=DBNAME)  # connecting to the database
    c = db.cursor()
    # dividing the sql to avoid long lines >80
    sql_str = "select articles.title as Article ,count(log.path) as Views from"
    sql_str = sql_str+" articles,log where log.path like '%'|| articles.slug||"
    sql_str = sql_str+" '%' and log.status='200 OK' group by articles.title"
    sql_str = sql_str+" order by Views desc limit 3;"
    c.execute(sql_str)
    sql_result = c.fetchall()
    db.close()
    print("The most popular three articles of all time :\n")
    for art in sql_result:
        print(art[0]+" - "+str(art[1])+"  views\n")
    print("\n\n")

    return None  # may be used later to test for errors


def get_pop_auth():
    """Add a post to the 'database' with the current timestamp."""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    sql_str = "select authors.name as Author ,count(log.path) as Views from "
    sql_str = sql_str+"authors,articles,log where authors.id=articles.author "
    sql_str = sql_str+"and log.path like '%'|| articles.slug|| '%' and log."
    sql_str = sql_str+"status='200 OK' group by authors.name order "
    sql_str = sql_str+" by Views desc ;"
    c.execute(sql_str)
    sql_result = c.fetchall()
    db.close()
    print("The  most popular article authors of all time :\n")
    for art in sql_result:
        print(art[0]+" - "+str(art[1])+"  views\n")
    print("\n\n")

    return None


def get_err_days():
    """Return all days with error in requests that exceed 1% of the total
    requests  considering all none "200 OK" as errors(n.b this is not so
    accurate but it will do the job) """
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    sql_str = "select to_char(total_req.date,'month dd,yyyy') as Date,((100 "
    sql_str = sql_str+"*bad_req.bad_req::float / total_req.total_req)::numeric"
    sql_str = sql_str+"(2,1)) as error_percent from bad_req join total_req "
    sql_str = sql_str+"on bad_req.date=total_req.date where (100 * bad_req.bad"
    sql_str = sql_str+"_req / total_req.total_req) > 1;"
    c.execute(sql_str)
    sql_result = c.fetchall()
    db.close()
    print("The  day(", "s) with  more than 1% of requests lead to errors :\n")
    for art in sql_result:
        print(art[0]+" - "+str(art[1])+"  % errors ")
    print("\n\n")

    return None


if __name__ == '__main__':
    reports = [get_pop_art, get_pop_auth, get_err_days]
    print("\n\nPROJECT: LOG ANALYSIS\n\n")
    print("a tool to analyze data in news database and display reports\n")
    for report in reports:
        ret_val = report()
    print("END OF REPORTS ")