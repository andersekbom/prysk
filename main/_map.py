from random import randint
from random import shuffle
import sqlite3
import classes
import os

print "Building the database...",

players = ["Red","Yellow","Green","Grey","Blue"]
## Randomize the order of the players
shuffle(players)

def initMap():

    ## Check if .db-file already exists
    try:
       with open('map.db'): 
       #if raw_input("Database exists, do you want to delete it? (y/n) >>)":
        ## Delete existing file
        os.remove('map.db')
    except IOError:
        pass

    conn = sqlite3.connect('map.db')
    c = conn.cursor()
    
    ## Open file with territories and starting troops
    terrFile = open("main/territories.txt")
    terrFileList = terrFile.readlines()
    shuffle(terrFileList)

    edgeFile = open("main/edges.txt")
    edgeFileList = edgeFile.readlines()
    for edgeTerr in edgeFileList:
        edgeList = edgeTerr.split(',')
        for i in range(1,len(edgeList):
            print 
            
            c.execute("INSERT INTO edges VALUES (?,?))",edges    



    # Create table
    c.execute('''CREATE TABLE territories
                 (name text, troops integer, owner text)''')

    c.execute('''CREATE TABLE edges
                 (name1 text, name2 text)''')
    
    ## Tell us what's going on
    #print "There are %s players." % len(players)
    #print "There are %s territories." % len(terrFileList)
    terrPerPlayer = divmod(len(terrFileList),len(players))
    #print "There are %s territories per player," % terrPerPlayer[0],
    #print "and %s extra.\n" % terrPerPlayer[1]
    
    ## Some inits
    i=0 # plain ol' counter
    l=0 # pointer for looping through territory list

    ## Loop through stuff, assigning territories as we go
    for player in players:
        for i in range (0,terrPerPlayer[0]):
            # Get next line from territories list
            terrLine = terrFileList[l].rstrip('\n'); l+=1
            terrName = terrLine.rstrip('\n,123')
            #terrTroops = terrLine.split(',')[1].rstrip('\n')
            terrTroops = randint(1,3)
            terrOwner = player

            # Insert a row of data
            terrData = (terrName, terrTroops, terrOwner)
            c.execute("INSERT INTO territories VALUES (?,?,?)",terrData)
            conn.commit()
            
    ## Distribute the remaining territories
    ## TODO: Evenly distribute the remaining territories (instead of bad like now)
    for i in range (0,terrPerPlayer[1]):

        terrLine = terrFileList[l].rstrip('\n'); l+=1
        terrName = terrLine.rstrip('\n,123')
        #terrTroops = terrLine.split(',')[1].rstrip('\n')
        terrTroops = randint(1,3)
        terrOwner = player

        # Insert a row of data
        terrData = (terrName, terrTroops, terrOwner)
        c.execute("INSERT INTO territories VALUES (?,?,?)",terrData)
        conn.commit()
        conn.close()

    print "Done!"

def setTroops(territory, troops):
    pass


def updateTerritory(territory, troops, owner):
    conn = sqlite3.connect('map.db')
    c = conn.cursor()
    c.execute("UPDATE territories SET owner = ?, troops = ? WHERE name = ?",(owner,troops,territory))
    conn.commit()
    conn.close()

def listAttTerritories(objPlayer):
    conn = sqlite3.connect('map.db')
    c = conn.cursor()
    c.execute("SELECT * FROM territories WHERE owner = ? AND troops > 1;",(objPlayer.name,))
    data = c.fetchall()
    conn.commit()
    conn.close()
    return data

def listDefTerritories(objPlayer):
    conn = sqlite3.connect('map.db')
    c = conn.cursor()
    c.execute("SELECT * FROM territories WHERE NOT owner = ? ORDER BY owner",(objPlayer.name,))
    data = c.fetchall()
    conn.commit()
    conn.close()
    return data

