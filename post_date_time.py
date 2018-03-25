from datetime import date,datetime
import sqlite3
def post_date_time(id,prd):
    conn=sqlite3.connect('datetime.db')     #detect_types=sqlite3.PARSE_DECLTYPES
    key=0            
    cursor=conn.execute('select '+str(prd)+' from date_time '+'WHERE Id='+str(id))
    for row in cursor:
        profile=row
    #if profile!=None:
    key=1
    if(key == 1):
        conn.execute('UPDATE date_time SET '+str(prd)+'=?'+' WHERE Id=?',(datetime.now(),str(id)))
    for row in cursor:
        profile=row
    conn.commit()
    conn.close()

#post_date_time(11,'p2')
#conn.execute("CREATE TABLE date_time (id integer primary key, p1 timestamp, p2 timestamp, p3 timestamp, p4 timestamp, p5 timestamp, p6 timestamp, p7 timestamp)")

#conn.execute('insert into date_time('+str(prd)+') values(?)'+' where id=?',(str(prd),datetime.now(),id))
#return  profile
#print(profile[0])

#conn.execute('UPDATE date_time SET '+str(prd)+'=?'+' WHERE Id=?',(datetime.now(),str(id)))


