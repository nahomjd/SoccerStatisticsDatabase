import requests
import csv
import json
import urllib2
from readCSV import upload

test = 0
database = "soccerDataSource"
#sample url to requests
#http://www.football-data.co.uk/new/ARG.csv
count = 0
#url of the webpage we start on
base = requests.get("http://www.football-data.co.uk/data.php")
#makes a list of each line of html
rows = base.text.split("\n")
#example
#http://www.football-data.co.uk/mmz4281/1819/E0.csv
baseURL = 'http://www.football-data.co.uk/'
for row in rows:
    #step 1 locating country link
    if '<tr><td><IMG' in row:
        #print row
        country = row.split("HREF=\"")[1].split("\">")[0]
        #print country
        #going in to country link
        r =requests.get("http://www.football-data.co.uk/" + country)
        
        #makes list of counry links
        lines = r.text.split("\n")
        for line in lines:
            #print line
            #line that the csv extension is on
            if '<IMG SRC="Excel' in line:
                field = line.split("HREF=\"")[1].split("\">")[0]
                
                link = baseURL + field
                csv_ = field.split("/", 1)[1]
                file = csv_.replace("/", "_")
                print 'field: ' + field
                print 'file name: ' + file
                print 'link to request: ' + link
                
                #data = requests.get(link)
                '''
                #print file
                f = open(file, 'wb')
                f.write(data.text.encode('ascii', 'replace'))
                f.close
                '''
                print file + " csv created!" + '\n'
                count += 1
                
                
                 
            if '.csv"><IMG' in line:
                field = line.split("HREF=\"")[1].split("\">")[0]
                
                link = baseURL + field
                file = field.split("/", 1)[1]
                
                print 'field: ' + field
                print 'file name: ' + file
                print 'link to request: ' + link
                '''
                data = requests.get(link)
            
                f = open(file, 'wb')
                f.write(data.text.encode('ascii', 'replace'))
                f.close
                '''
                print file + " csv created!" + '\n'
                count += 1
      
print count
 