import csv
import re
import pymysql
import glob

tablename = 'soccerDataSource'

conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='nahomjd', passwd='X7phenom5!', db='nahomjd_is426', autocommit=True) #setup our credentials
cur = conn.cursor(pymysql.cursors.DictCursor)

inputs = []  # etc
count = 0

for files in glob.glob('C:/Users/User/Desktop/FinalProject/backupCSVs/*E0.csv'):
    inputs.append(files)
    print files

#determine field names 
fieldnames = []
for filename in inputs:
  with open(filename, "r") as f_in:
    reader = csv.reader(f_in)
    headers = next(reader)
    for header in headers:
      if header not in fieldnames:
        if len(header) > 0:
            fieldnames.append(header)
            count += 1
            print header


sql = "CREATE TABLE IF NOT EXISTS `"+tablename+"` ("
i=0
c2m = {}
m2c = {}

for field in fieldnames:
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

conn.close()

