import csv
import re
import pymysql
from dateConverter import format
count = 0
#9900 should be 380
#9394 462
#9495 462
#9596 380
#9697 380

def upload(filename, tablename):        
    count = 0
    conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='nahomjd', passwd='*******', db='nahomjd_is426', autocommit=True) #setup our credentials
    cur = conn.cursor(pymysql.cursors.DictCursor)

    with open(filename) as f:
        data = [{k: str(v) for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]
    
    
    fields = data[0].keys()
    date = ""
    sql = "CREATE TABLE IF NOT EXISTS `soccerDataSource` ("
    
    

    failure = 0
    i=0
    c2m = {}
    m2c = {}
    for field in fields:
        
        if field == "":
            failure += 1
        else:    
            fn = field.lower().replace(" ","_")
            fn = field.lower().replace("    ","")
            
            c2m[field] = fn
            m2c[fn] = field
            if i > 0:
                sql+= ",\n"
            sql += "`"+fn+"`" + " VARCHAR(255) NULL"
            i+=1
    sql += ") ;"
   
    cur.execute(sql)

    f = open("mytable.sql",'w')
    f.write(sql)
    f.close()

    fl = '`,`'.join(m2c.keys())
    fl = '`' + fl + '`'
    tl = ''

    tl = str('%s,' * len(m2c.keys()))[0:-1]

    #print fl
    #print tl


    sql = 'INSERT INTO `'+tablename+'` ('+fl+') \
    VALUES ('+tl+');'
    #print sql


    
    for row in data:
        data_ok = False
        fdl = []
        for fn in m2c.keys():
            if fn == 'date':
                
                date = format(row[m2c[fn]])
                if len(date) > 0:
                    data_ok = True
                    fdl.append(date)
                    count += 1
            else:
                fdl.append(row[m2c[fn]])
        #print sql
        #print fdl
        if data_ok:
            #print sql
            cur.execute(sql,fdl)
    print count
    cur.close()
    conn.close()
    #print "failed columns" + str(failure)