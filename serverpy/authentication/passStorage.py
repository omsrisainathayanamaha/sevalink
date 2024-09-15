# Sairam! Sri Gurubyo Namaha!
# passStorage.py
# Author: Sahanav Sai Ramesh
# Description: Methods for storage of the passwords
# Version Alpha

from passRetrieve import format
from passRetrieve import checkUserExistence
import serverpy.serverConstants as sc

# If user exists, returns -1. If error, returns 0, Else returns 1
def storeUser(username, pwd):
    if(checkUserExistence(username)):
        return -1
    logStr = format(username,pwd)
    try:
        open(sc.PASS_DOCUMENT).write(logStr+"\n")
    except(OSError):
        return 0
    return 1


    

