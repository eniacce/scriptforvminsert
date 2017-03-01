#!/usr/bin/python
# -*- coding: utf-8 -*-
import psycopg2
import sys
import time


con = None

try:

    con = psycopg2.connect("dbname='postgres' user='postgres' password='123456' host='185.144.14.20'");
    cur = con.cursor();
    while True:
     start_time = time.time()
     cur.execute("INSERT INTO test2(ad,zaman) VALUES('mesut',now())");
     con.commit()
     end_time = time.time()
     print 'Yazma suresi %s'  % (end_time-start_time)

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
