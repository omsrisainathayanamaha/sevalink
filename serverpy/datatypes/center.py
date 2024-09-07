# Sairam! Om Sri Gurubyo Namaha!
# center.py
# Author: Sahanav Sai Ramesh
# Purpose: Representation of a Chinmaya Mission Center
# Version Alpha
# Dedicated to Gurudev's Feet
from serverpy.datatypes.member import Member
from serverpy.datatypes.project import Project
class Center:
    def __init__(self, name:str, centerLoc:tuple[float]):
        self.name = name
        self.members:list[Member] = []
        self.centerLoc:tuple[float] = centerLoc
        self.projects = list[Project] = []