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
import wx

def main():
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

    #Create a desktop notification to inform the operator that prices are soon to expire for
    #  listed vendors.
    app = wx.App(False)
    frame = MainWindow(None, "Expiration Notifier")
    app.MainLoop()

    #Output a python desktop notification to inform the operator of the incoming
    # expiration date and confirm whether they want to send an email to the vendor.
    print "The expired vendor table:"
    for row in results:
        print ("Vendor: " + row[0] + "  ExpirationDate: " + row[1])

    for row in results:
        print ("Vendor: " + row[0] + "  ExpirationDate: " + row[1])

    connection.close()

class MainWindow(wx.Frame):
       def __init__(self, parent, title):
         wx.Frame.__init__(self, parent, title=title, size=(200,100))
         self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
         self.CreateStatusBar() # A Statusbar in the bottom of the window

         # Setting up the menu.
         filemenu= wx.Menu()

         # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
         menuAbout = filemenu.Append(wx.ID_ABOUT, "&About", Information about this program)
         menuExit = filemenu.Append(wx.ID_EXIT, "&Exit", Terminate the program)

         #Create the menu bar
         menuBar = wx.MenuBar()
         menuBar.Append(filemenu, "&File")
         self.SetMenuBar(menuBar)

         #Set events
         self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
         self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

         self.Show(True)

        def OnAbout(self,e):
             # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
             dlg = wx.MessageDialog( self, "A small text editor", "About Sample Editor", wx.OK)
             dlg.ShowModal() # Show it
             dlg.Destroy() # finally destroy it when finished.

       def OnExit(self,e):
            self.Close(True)  # Close the frame.



#Execute the main function
if __name__ == '__main__':
    main()
