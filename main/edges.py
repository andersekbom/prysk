import sqlite3

conn = sqlite3.connect('map.db')
c = conn.cursor()

#c.execute('''CREATE TABLE edges (name1 text, name2 text)''')
#conn.commit()

i=0
edgeFile = open("main/edges.txt")
edgeFileList = edgeFile.readlines()
for edgeTerr in edgeFileList:
    edgeList = edgeTerr.split(',')
    for i in range(1,len(edgeList)):
        print "INSERT INTO edges VALUES (%s,%s)" % (edgeList[0],edgeList[i].rstrip('/n'))
        
        edges = (edgeList[0],edgeList[i].rstrip('/n'))
        c.execute("INSERT INTO edges VALUES (?,?)",edges)
        conn.commit()

