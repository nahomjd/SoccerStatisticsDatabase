import csv
import re
import pymysql

        
conn = pymysql.connect(host='mysql.clarksonmsda.org', port=3306, user='nahomjd', passwd='*******', db='nahomjd_is426', autocommit=True) #setup our credentials
curall = conn.cursor(pymysql.cursors.DictCursor)

sql = 'SELECT * FROM `soccerDataSource` ORDER BY `date`;'
curall.execute(sql)


#referee data
refList = [[],[],[]]
refListU = [[],[],[]]

teamList = []
teamListU = []
comma = set(',')
t = 0
t2 = 0
ref = False
team = False 
game = False
stats = True

if ref:
    for row in curall:
        if row['referee']:
            count = row['referee'].count(' ')
            #dealing with last name first
            if ',' in row['referee']:
                
                refList.append([row['referee'].split(" ")[1], row['referee'].split(",")[0], row['referee']])
                
            else:
                #if len(row['referee'].split(" ")[0]) > 1:
                #print row['referee'].split()
                #dealing with middle intial
                if len(row['referee'].split()) == 3:
                    refList.append([row['referee'].split(" ")[0], row['referee'].split(" ")[2],row['referee']])
                elif len(row['referee'].split()) == 2:
                    refList.append([row['referee'].split(" ")[0], row['referee'].split(" ")[1],row['referee']])
                else:
                    print "error"
            t += 1        
            
        #gets rid of duplicates
        for input in refList:
            if input not in refListU:
                t2 += 1
                refListU.append(input)
                print input[1] + " not duplicate"
               
    print t, t2

    #print refListU  
    #insert list
    for name in refListU:
        if len(name) != 0: 
            #print name
            print name[0] +" "+ name[1] + " " + name[2]
            curwareInsert = conn.cursor(pymysql.cursors.DictCursor)
            
            sql = 'INSERT INTO referee (`fName`,`lName`, `Original`) VALUES \
            (%s,%s,%s);'
            curwareInsert.execute(sql,(name[0],name[1],name[2]))
            print "intserted"
         
         
if team:
    for row in curall:
        if row['hometeam']:
            #print row['hometeam']
            teamList.append(row['hometeam'])
        if row['hometeam']:
            #print row['hometeam']
            teamList.append(row['awayteam'])
        #gets rid of duplicates
        for input in teamList:
            if input not in teamListU:
                t2 += 1
                teamListU.append(input)
                print input + " not duplicate"
    #upload teams            
    for name in teamListU:
        if len(name) != 0: 
            #print name
            print name
            curwareInsert = conn.cursor(pymysql.cursors.DictCursor)
            
            sql = 'INSERT INTO teams (`team`) VALUES \
            (%s);'
            curwareInsert.execute(sql,(name))
            print "intserted"
            
            
if game:
    hTeamID = 0
    aTeamID = 0
    
    for row in curall:
        sql = 'SELECT * FROM `teams` WHERE team = %s'
        #getting hometeam ID
        curteam = conn.cursor(pymysql.cursors.DictCursor)
        curteam.execute(sql,(row['hometeam']))
        for team in curteam:
            htid = team['teamID']
            
        sql = 'SELECT * FROM `teams` WHERE team = %s'
        #getting awayteam ID
        curteam = conn.cursor(pymysql.cursors.DictCursor)
        curteam.execute(sql,(row['awayteam']))
        for team in curteam:
            atid = team['teamID']
        curwareInsert = conn.cursor(pymysql.cursors.DictCursor)
            
        sql = 'INSERT INTO game (`date`,`division`,`homeTeamID`,`awayTeamID`) VALUES \
        (%s,%s,%s,%s);'
        curwareInsert.execute(sql,(row['date'],row['div'],htid, atid))
        print "intserted"
        
if stats:
    
    for row in curall:
        rid = 0
        
        if row['referee'] is not None:
            sql = 'SELECT * FROM `referee` WHERE `Original` = %s'
            #print row['referee']
            curgame = conn.cursor(pymysql.cursors.DictCursor)
            curgame.execute(sql,(row['referee']))
            
            for ref in curgame:
                rid = ref['refID']
            curwareInsert = conn.cursor(pymysql.cursors.DictCursor)
            sql = 'INSERT INTO `stats` (`refID`,`result`,`homeFinalGoals`,`awayFinalGoals`,`homeHalfGoals`,\
            `awayHalfGoals`,`halfTimeResult`,`attendance`,`homeShots`,`awayShots`,`homeShotsOnTarget`,`awayShotsOnTarget`,\
            `homeHitWoodwork`,`awayHitWoodwork`,`homeYellowCards`,`awayYellowCards`,`homeRedCards`,`awayRedCards`,\
            `homeCorners`,`awayCorners`,`homeFoulsCommitted`,`awayFoulsCommitted`,`homeOffsides`,`awayOffsides`)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            print rid
            curwareInsert.execute(sql,(rid,row['ftr'],row['fthg'],row['ftag'],row['hthg'],row['htag'],row['htr']\
            ,row['attendance'],row['hs'],row['as'],row['hst'],row['ast'],row['hhw'],row['ahw'],row['hy'],row['ay']\
            ,row['hr'],row['ar'],row['hc'],row['ac'],row['hf'],row['af'],row['ho'],row['ao']))
            print "intserted"
        else:
            curwareInsert = conn.cursor(pymysql.cursors.DictCursor)
            sql = 'INSERT INTO `stats` (`result`,`homeFinalGoals`,`awayFinalGoals`,`homeHalfGoals`,\
            `awayHalfGoals`,`halfTimeResult`,`attendance`,`homeShots`,`awayShots`,`homeShotsOnTarget`,`awayShotsOnTarget`,\
            `homeHitWoodwork`,`awayHitWoodwork`,`homeYellowCards`,`awayYellowCards`,`homeRedCards`,`awayRedCards`,\
            `homeCorners`,`awayCorners`,`homeFoulsCommitted`,`awayFoulsCommitted`,`homeOffsides`,`awayOffsides`)\
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
            
            curwareInsert.execute(sql,(row['ftr'],row['fthg'],row['ftag'],row['hthg'],row['htag'],row['htr'],\
            row['attendance'],row['hs'],row['as'],row['hst'],row['ast'],row['hhw'],row['ahw'],row['hy'],row['ay']\
            ,row['hr'],row['ar'],row['hc'],row['ac'],row['hf'],row['af'],row['ho'],row['ao']))
            print "intserted"
       
        
        