import sqlite3
import io
from sqlite3 import Error

con = sqlite3.connect('db.sqlite3')
with io.open('backupdatabase_dump.sql','w') as p:
    for line in con.iterdump():
        p.write('%s\n' % line)

print('Backup hecha')
con.close()
        