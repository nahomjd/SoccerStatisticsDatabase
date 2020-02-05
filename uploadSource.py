import requests
import csv
import json
import urllib2
import glob
from readCSV import upload
import pymysql

conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='nahomjd', passwd='********', db='nahomjd_is426', autocommit=True) #setup our credentials
curall = conn.cursor(pymysql.cursors.DictCursor)

database = "soccerDataSource"
trun = conn.cursor(pymysql.cursors.DictCursor)
sql = 'TRUNCATE TABLE `soccerDataSource`;'
trun.execute(sql)

for files in glob.glob('C:/Users/User/Desktop/FinalProject/backupCSVs/*_E0.csv'):
   
    field = files.split('\\')[1]
    print field
    upload(files, database)
    print "uploaded"