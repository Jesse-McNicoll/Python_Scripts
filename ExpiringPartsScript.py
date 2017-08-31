#!/usr/bin/env python27

# Title: ExpiringPartsScript.py
# Author: Jesse McNicoll
# Date Created: 8/23/2017
# Description:
#   This script will query the erpsql server and run a query to find expiring vendor costs.
#   If any vendors are expiring within the next six weeks, the script will automatically send an
#   email to their point of contact asking for new prices.
#

import pyodbc

#Set database and server variables so the code is easily portable
server = 'ERPSQL'
database = 'EpicorTest10'

#Create a string to input to the pyodbc connnection method.  Creating it allows it to be formatted with
# the correct database.
connection_string = 'Driver={SQL Server};Server=ERPSQL;Database=%s;Trusted_Connection=yes;' % (database)

#Create a
query_string = '''SELECT     T1.VendorID, T1.ExpirationDate
FROM         (SELECT     %(db)s.dbo.Vendor.VendorID, MAX(%(db)s.Erp.VendPart.ExpirationDate) AS ExpirationDate
              FROM          %(db)s.Erp.VendPart INNER JOIN
              %(db)s.dbo.Vendor ON %(db)s.Erp.VendPart.VendorNum = %(db)s.dbo.Vendor.VendorNum
              GROUP BY %(db)s.dbo.Vendor.VendorID) AS T1
WHERE     (ExpirationDate <= DATEADD(month, 1, GETDATE()))''' % {'db': database}

print query_string
#connection = pyodbc.connect(conn_str)
connection = pyodbc.connect(connection_string)
cursor = connection.cursor()

cursor.execute (query_string)

results = cursor.fetchone()

print "The expired vendor table:"

while results:
    print ("Vendor: " + results[0] + "ExpirationDate" + results[1])

results = cursor.fetchone()
connection.close()
