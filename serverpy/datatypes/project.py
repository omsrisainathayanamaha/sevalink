# Sairam! Sri Gurubyo Namaha!
# project.py
# Author: Sahanav Sai Ramesh
# Purpose: Represents a Project that a Center creates and manages
# Version Alpha
# Dedicated to Swamiji's Feet
from appointment import Appointment
class Project:
    def __init__(self, name:str):
        self.name:str = name
        self.appointments:list[Appointment] = []
        self.description:str = ""
    def addAppointment(self, app:Appointment):
        self.appointments.append(app)
    def addDescription(self, description:str):
        self.description = description