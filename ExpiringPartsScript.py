#!/usr/bin/env python27

# Title: ExpiringPartsScript.py
# Author: Jesse McNicoll
# Date Created: 8/23/2017
# Description:
#   This script will query the erpsql server and run a query to find expiring vendor costs.
#   If any vendors are expiring within the next six weeks, the script will automatically send an
#   email to their point of contact asking for new prices.
#

import MySQLdb

connection = MySQLdb.connect(host="ERPSQL",db="Epicor10")

cursor = connection.cursor()

cursor.execute ("SELECT VendorID, ExpirationDate FROM Epicor10.dbo.Vendor.VendorID")

results = cursor.fetchone()

print "The expired vendor table:"

while results:
    print ("Vendor: " + results[0] + " ExpirationDate: " + str(results[1]))

results = cursor.fetchone()
connection.close()
