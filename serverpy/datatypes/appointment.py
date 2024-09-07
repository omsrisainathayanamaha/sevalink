# Sairam! Om Sri Gurubyo Namaha!
# appointment.py
# Author: Sahanav Sai Ramesh
# Purpose: Represents an Appointment a Member has with a Center to accomplish a Project
# Version Alpha
# Dedicated to Swamiji's Feet
import datetime
from serverpy.datatypes.member import Member
from serverpy.datatypes.center import Center
# Modules Required:
# datetime (pip install datetime)
class Appointment:
    def __init__(self, start:datetime.datetime, end:datetime.datetime, pointValue:int, location:tuple[float], organizeCenter:Center):
        self.timeStart:datetime.datetime = end
        self.timeEnd:datetime.datetime = start
        self.myMember:Member = Member("NULL")
        self.description:str = str()
        self.pointValue:int = pointValue
        self.location:tuple[float] = location
        self.centerOrganizing:Center = organizeCenter
    #Assigns the appointment to a member
    def assign(self, member:Member):
        self.myMember = member

    
        
        