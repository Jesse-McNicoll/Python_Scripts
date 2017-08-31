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

#Create a string for the query that can be easily updated with a new database, allowing mutability of code.
query_string = '''SELECT     T1.VendorID, T1.ExpirationDate
FROM         (SELECT     %(db)s.dbo.Vendor.VendorID, MAX(%(db)s.Erp.VendPart.ExpirationDate) AS ExpirationDate
              FROM          %(db)s.Erp.VendPart INNER JOIN
              %(db)s.dbo.Vendor ON %(db)s.Erp.VendPart.VendorNum = %(db)s.dbo.Vendor.VendorNum
              GROUP BY %(db)s.dbo.Vendor.VendorID) AS T1
WHERE     (ExpirationDate <= DATEADD(month, 1, GETDATE()))''' % {'db': database}

#Now, use the connection string as the input to the pyodbc.connect() method to
# to form the database connection.
connection = pyodbc.connect(connection_string)
#Instantiate a cursor to the connection to allow a query to be performed.
cursor = connection.cursor()
#Execute the query_string with cursor.execute() method to get the expiring vendor data.
cursor.execute (query_string)
#Obtain all the results to allow them to be parsed through.
results = cursor.fetchall()

#Output a python desktop notification to inform the operator of the incoming
# expiration date and confirm whether they want to send an email to the vendor.
print "The expired vendor table:"
for row in results:
    print ("Vendor: " + row[0] + "  ExpirationDate: " + row[1])

for row in results:
    print ("Vendor: " + row[0] + "  ExpirationDate: " + row[1])



connection.close()
