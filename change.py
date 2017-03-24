#!/usr/bin/python
#-*- coding: utf-8 -*-
import sqlite3

#Connect to database
#If the database doesn't exist, then it will be created.
db = sqlite3.connect('test.db');
print "To open database is successful";

#Show data in database
begin = db.execute("select * from CHANGEDATA")
for row in begin:
    print "ID: " , row[0]
    print "Article: " , row[1]

#Let the user inputs
whichID = raw_input("Which data do you want to change, for all(0): ")
before = raw_input("Please enter the string you want to modify: ")
after = raw_input("Please enter the modified string: ")

db.text_factory = lambda x: x.decode("utf-8")

if whichID != '0' :
    choose = db.execute("select * from CHANGEDATA where ID=?",whichID)
else: 
    choose = db.execute("select * from CHANGEDATA")

for row in choose:
    sentence = row[1].replace(before,after)
    db.execute("update CHANGEDATA set ARTICLE=? where id=?",(sentence,row[0]))
    db.commit()

end = db.execute("select * from CHANGEDATA")
for row in end:
    print "ID: " , row[0]
    print "Article: " , row[1]

#Close the connection
db.close();
