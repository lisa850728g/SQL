#!/usr/bin/python
import sqlite3

#Connect to database: test.db.
#If the database doesn't exist, then it will be created.
db = sqlite3.connect('test.db');
print "To open database is successful";

#Create a table
#db.execute('''CREATE TABLE READFILE
    #(ID         INTEGER PRIMARY KEY,
    #ARTICLE     TEXT NOT NULL,
    #BEFORE      TEXT NOT NULL,
    #AFTER       TEXT NOT NULL);''')
#print "To create table is successful";

#Open the input file
infile = raw_input("Please enter the file you want to read: " )
infile = open (infile)

#Read file
fileString = infile.read()

#User input
before = raw_input("Please enter the string want to be changed: ")
after = raw_input("Please enter the string want to change to: ")

#Replace the string
fileString = fileString.replace(before,after)

#Close the file
infile.close()

db.text_factory = lambda x: x.decode("utf-8")

#Insert a row of data
db.execute("insert into READFILE (ID,ARTICLE,BEFORE,AFTER) VALUES(NULL,?,?,?)"
                ,(fileString,before,after))
##Save the changes
db.commit()

#Show every data in database
getData = db.execute("select * from READFILE")
for row in getData:
    print "ID: " , row[0]
    print "Article: \n" , row[1]
    print "Before: " , row[2]
    print "After: " , row[3]

#Close the connection
db.close();
