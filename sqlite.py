#!/usr/bin/python
#-*- coding: utf-8 -*-
import sqlite3

#Connect to database: test.db.
#If the database doesn't exist, then it will be created.
db = sqlite3.connect('test.db');
print "To open database is successful";

#Create a table
#db.execute('''CREATE TABLE CHANGEDATA
    #(ID         INTEGER PRIMARY KEY,
    #ARTICLE     TEXT NOT NULL);''')
#print "To create table is successful";

#Let the user inputs
print "Please enter the strings :"
sentence = ""
while True:
    sen = raw_input()
    if sen is ";":
        break
    else:
        sentence += sen + "\n"

db.text_factory = lambda x: x.decode("utf-8")

#Insert a row of data
db.execute("insert into CHANGEDATA  VALUES(NULL,?)",(sentence.rstrip(),))
#Save the changes
db.commit()

#Show every data in database
getData = db.execute("select * from CHANGEDATA")
for row in getData:
    print "ID: " , row[0]
    print "Article: \n" , row[1]

#Close the connection
db.close();
