'''
Created on 06.03.2016

@author: cypher9
'''
from datetime import datetime
from data.event import make_event

class Functions(object):
    '''
    classdocs
    '''
    def __init__(self, eventlist):
        self.eventlist = eventlist
        

    def add_event_to_list(self, event):
        self.eventlist.append(event)
    
    def view_events(self):
        for event in self.eventlist:
            print(event.event_title + "\n")
            print(event.event_description)
            
    def add_event(self):
        print("Add your event details:\n")
        try:
            event_title=str(raw_input('Title: '))
            event_description = ""
            stopword = ""
            first = True
            while True:
                if first:
                    line = raw_input('Description: ')
                    first = False
                else:
                    line = raw_input()
                if line.strip() == stopword:
                    break
                event_description += "%s\n" % line
            event_start_date = str(raw_input("Startdate(YYYY-MM-DD): "))
            event_start_time = str(raw_input("Starttime(HH:MM)24h: "))
            event_end_date = str(raw_input("Enddate(YYYY-MM-DD): "))
            event_end_time = str(raw_input("Endtime(HH:MM)24h: "))
            event_start_datetime = datetime.strptime(event_start_date + ' ' + event_start_time, '%Y-%m-%d %H:%M')
            event_end_datetime = datetime.strptime(event_end_date + ' ' + event_end_time, '%Y-%m-%d %H:%M')
        except ValueError:
            print "Not a valid input..." 
               
        try:
            self.add_event_to_list(make_event(event_title, event_description, event_start_datetime, event_end_datetime))          
        except Exception:
            print "Error generating event..."