# Sairam! Om Sri Gurubyo Namaha!
# member.py
# Author: Sahanav Sai Ramesh
# Purpose: Represents a Member of Chinmaya Mission
# Version Alpha
# Dedicated to Swamiji's Feet
from serverpy.datatypes.center import Center
from serverpy.datatypes.appointment import Appointment
class Member:
    def __init__(self, name:str, username:str):
        self.myCenter:Center = Center()
        self.name:str = name
        self.username:str = username
        self.appointments:list[Appointment] = []
    def setCenter(self, c:Center):
        self.myCenter = c