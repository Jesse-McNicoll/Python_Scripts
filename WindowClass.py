import wx

def main():
	
	
	app = wx.App(False)
	vendorList = ['DREAGERS', 'AFC', '3MCOMPAN', 'SAFTECH', 'MCDONALD', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH', 'SAFTECH']
	
	frame = MainWindow(None, "Expiration Notifier", vendorList)
	app.MainLoop()






class MainWindow(wx.Frame):

	#Define the constructor class
	def __init__(self, parent, title, vendorList = []):
		super(MainWindow, self).__init__(parent, title=title, 
		size = (400,300), style = wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CLOSE_BOX | wx.CAPTION)
		#Center the application on the monitor to allow for easy reading by user.  
		self.Centre()
				
		#Create the scrollWindow for the application to allow for user input
		#scrollWindow = wx.scrollWindow(self)
		#Create a scrolled window to allow for viewing of multiple vendors.
		splitWindow = wx.SplitterWindow(self, -1)
		splitWindowSizer = wx.BoxSizer(wx.VERTICAL)
		panel = wx.Panel(splitWindow)
		
		scrollWindow = wx.ScrolledWindow(splitWindow)
		
		splitWindow.SplitHorizontally(scrollWindow,panel, 180)
		splitWindow.SetSizer(splitWindowSizer)
		#Prevent user from resizing the windows
		splitWindow.SetSashInvisible()
		
		#Set the scroll bars to allow scrolling
		scrollWindow.SetScrollbars(20,50,55,40)

#This section implements the scroll window of the app		
		#Create the menu with an options button to allow for...options
		menuBar = wx.MenuBar()
		OptionsButton = wx.Menu()
		
		#Create an option to exit the application
		exitItem = wx.MenuItem(OptionsButton,wx.ID_EXIT,'Quit\tCtrl+Q')
		OptionsButton.Append(exitItem)
		
		#Add the options button to the menu bar
		menuBar.Append(OptionsButton, 'Options')
		#Apply the menu bar 
		self.SetMenuBar(menuBar)
		self.Bind(wx.EVT_MENU, self.Quit, exitItem)
		
		informationTitle = wx.StaticText(scrollWindow, -1, 'Expiring Vendors:', (3,3))
		
		#Execute a for loop to add check boxes to the GUI as necessary
		y_size = 20
		var = 0
		checkBox = wx.CheckBox(scrollWindow, -1, "Send to all listed vendors", (20,y_size), (160, -1))
		y_size += 20
		#Set a sizer to add a scroll bar for cases of many vendors
		scrollWindowSizer = wx.BoxSizer(wx.VERTICAL)
		scrollWindowSizer.Add(checkBox, 1, wx.EXPAND)
		
		#Loop through the vendors that are expired to place a check box for each on the main screen.
		for vendor in vendorList:
					checkBox = wx.CheckBox(scrollWindow, -1, vendor, (20,y_size), (160, -1))
					#Add 20 to the y-coordinate to get to the next line
					y_size += 20
					#Add the checkbox to the sizer to continually change the needed size.
					scrollWindowSizer.Add(checkBox, var, wx.ALL, 5)
					
					
		#Now, set the scrollWindow to the scrollWindowSizer to allow for the appearance of the scroll bar.
		#scrollWindow.SetSizer(scrollWindowSizer)
		
		
#This section sets the panel portion of the app
		emailButton = wx.Button(panel, -1, 'Send Pricing Email to Selected Vendors')
		btnSizer = wx.BoxSizer(wx.HORIZONTAL)
		btnSizer.Add(emailButton,1, wx.ALIGN_CENTRE_VERTICAL)
		panel.SetSizer(btnSizer)
		#Show the app on the screen
		self.Show()
		
	def Quit(self, e):
		self.Close()
		
		  

 



#Execute the main function
if __name__ == '__main__':
    main()