'''
Created on 06.03.2016

@author: cypher9
'''

class Info(object):
    '''
    Info of version and tool
    '''
    def start_text(self):
        print("PyPlanner v0.0.5-beta")
        print("--")
        print("PyPlanner is a simple commandline tool for keeping up with your appointments and events")
        print("PyPlanner encrypts your database with gpg to make your stuff really private ")
        print("\n")
        
    def help(self):
        print("\nhelp for PyPlanner")
        print("you have 6 options to select from:\n")
        print("1 - Add an event")
        print("2 - Search")
        print("3 - View")
        print("4 - Delete")
        print("5 - Show calendar")
        print("6 - Help")
        print("0 - Quit \n")
        
        print("Option 1 - Add an event         : Add a new event to an existing calendar or create a new one\n")
        
        print("Option 2 - Search:")
        print("Option 2 - 1 - Search by string : Search all events_titles and event_descriptions for a specified string")
        print("Option 2 - 2 - Search by date   : Search all events on one specified date")
        print("Option 2 - 0 - Main menu        : Return to main menu\n")
        
        print("Option 3 - View:")
        print("Option 3 - 1 - View calendars   : View all existing calendars")
        print("Option 3 - 2 - View events      : View all events from one specified calendar\n")
        print("Option 3 - 0 - Main menu        : Return to main menu\n")
        
        print("Option 4 - Delete:")
        print("Option 4 - 1 - Delete calendar  : Delete one calendar with all its content")
        print("Option 4 - 2 - Delete event     : Delete one single event\n")
        print("Option 4 - 0 - Main menu        : Return to main menu\n")
        
        print("Option 5 - Show calendar        : Display Year or Month calendar\n")
        
        print("Option 6 - Help                 : Display this help\n")
        
        print("Option 0 - Quit                 : Exit PyPlanner")        
        
        raw_input("Press ENTER to go on...")
        
        
    def menu(self):
        print("\nSelect what you want to do")
        print("1 - Add an event")
        print("2 - Search")
        print("3 - View")
        print("4 - Delete")
        print("5 - Show calendar")
        print("6 - Help")
        print("0 - Quit")
        
    def submenu_view(self):
        print("\nSelect what you want to do")
        print("1 - View calendars")
        print("2 - View events")
        print("0 - Main Menu")
        
        return int(raw_input('Option: '))
        
    def submenu_delete(self):
        print("\nSelect what you want to do")
        print("1 - Delete calendar")
        print("2 - Delete event")
        print("0 - Main Menu")
        
        return int(raw_input('Option: '))
    
    def submenu_search(self):
        print("\nSelect what you want to do")
        print("1 - Search by string")
        print("2 - Search by date")
        print("0 - Main Menu")
        
        return int(raw_input('Option: '))
        