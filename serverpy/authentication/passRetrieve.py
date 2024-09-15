# Sairam! Sri Gurubyo Namaha!

# passRetrieve.py

# Author: Sahanav Sai Ramesh
# Purpose: Stores and retrieves the passwords from memory.
# Version Alpha
# Dedicated to Pujya Gurudev and Swamiji's lotus feet.

import serverpy.serverConstants
import string
# Modules Required: string

# format(username, password) where both parameters are strings
# Precondition: username is a valid username
# Postcondition: the format string in the form username,password to search the file using
def format(username:str, password:str):
    username.translate(None, " \n\t\r")
    return f"{username},{password}"

# formatusername(username) where the username parameter is a string
# Precondition: username is a valid username
# Postcondition: the username is formatted in a manner that can be used to search the file
def formatusername(username:str):
    return f"{username.translate(None, " \n\t\r")}"

# checkUserExistence(username) where the username parameter is a string
# Precondition: username is a valid, formatted username that has been run through formatusername(username)
# Postcondition: a boolean that represents if the user's account exists or not
def checkUserExistence(username:str):
    try:
        open(serverpy.serverConstants.PASS_DOCUMENT).read().index(username)
    except ValueError:
        return False
    return True

def checkLogin(username:str, password:str):
    formatted = format(username, password)
    f = open(serverpy.serverConstants.PASS_DOCUMENT)
    for i in f:
        if i == formatted:
            return True
    return False

# Returns -1 if the user already exists
def createPerson(username:str, password:str):
    if(checkUserExistence(username)):
        return -1
    formatted = format(username, password)
    f = open(serverpy.serverConstants.PASS_DOCUMENT, 'a')
    f.write(formatted+"\n")
