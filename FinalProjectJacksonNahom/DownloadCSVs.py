import requests
import csv
import json
import urllib2
from readCSV import upload

test = 0
database = "soccerDataSource"
#http://www.football-data.co.uk/new/ARG.csv
count = 0
base = requests.get("http://www.football-data.co.uk/data.php")
#glob function
rows = base.text.split("\n")
#http://www.football-data.co.uk/mmz4281/1819/E0.csv
baseURL = 'http://www.football-data.co.uk/'
for row in rows:
    if '<tr><td>' in row:
        country = row.split("HREF=\"")[1].split("\">")[0]
        #print country
    
        r =requests.get("http://www.football-data.co.uk/" + country)
    
        lines = r.text.split("\n")
        for line in lines:
            #print line
            if '<IMG SRC="Excel' in line:
                field = line.split("HREF=\"")[1].split("\">")[0]
                
                link = baseURL + field
                csv_ = field.split("/", 1)[1]
                file = csv_.replace("/", "_")
                print file
                
                data = requests.get(link)
                
                
                
                
                
                #print file
                f = open(file, 'wb')
                f.write(data.text.encode('ascii', 'replace'))
                f.close
                
                print file + " csv created!"
                count += 1
                
                
                 
            if '.csv"><IMG' in line:
                field = line.split("HREF=\"")[1].split("\">")[0]
                
                link = baseURL + field
                file = field.split("/", 1)[1]
                
                print file
                data = requests.get(link)
            
                f = open(file, 'wb')
                f.write(data.text.encode('ascii', 'replace'))
                f.close
                
                print file + " csv created!"
                count += 1
      
print count
 