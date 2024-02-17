"""
    Get Prepared for The Whackiest Code Ever, And for that Same Reason, Keep your Eyes on the Comments Given
    by me, So you Don't Get Drowned in this Hole of Bad Code Also :).
"""

# Importing Essential Module + Extra (to Delete a File at the end).
from subprocess import getoutput # Creating child Processes Using this Module
from os import remove # Deletes a File that you can specify

def get_name():
    """ Requests an Input, for Indication of the Target Wi-Fi Network for Password Recovery. """
    target = input("\nHello, World!\nPlease Enter the Target Wi-Fi Network's SSID:\n>> ") # Requesting Input Values from User.
    global NAME
    NAME = target
    
    return target

def get_pass(name=get_name()):
    """ Acquires the PassKey of the Target Wi-Fi Network, Requires Input from the User, Which is Covered by get_name Function. """
    data = getoutput(f"netsh wlan show profile \"{name}\" key=clear") # Running the command Essential to Get the Saved Password, as a Child Process.
    
    # This will write all the Data Recieved from the Child Process, to a Temporary file in Order to Check and Get some Values from it Later On.
    with open("key", "w") as f: 
        f.write(data)
    
    # This will Read the Data Written on the Temporary File, to see if the Target Wi-Fi Network is Actually Password Protected or Not.
    with open("key", "r") as f:
        lines = f.readlines() # All the Lines written in the Temp File, as a List, that Its Indexes indicate Each Line on the File.
        
        # Checking a Value in Line 28 of the File (This line says if the Network is Pass Protected or Not).
        if lines[27] == '    Authentication         : Open\n':
            return False # if that line Contained some Special Text (That only Unprotected Networks have), Then that Network is Un-Protected.
        
        # But if it got another Special Text in Line 33 of the Temp File, Then it Indicates that the Target Network is Indeed, Protected.
        else:
            return lines[32].replace("    Key Content            : ", "").replace("\n", "")

# The Result, IT Has To get Shown to The User, Isn't it?
if get_pass() == False:
    print("\n\t-!-the Target Wi-Fi Network is Not Password-Protected-!-")

else:
    print("==========")
    print(f"\nPassword, Found for Wi-Fi Network \"{NAME}\" is:\n\t{get_pass()}")

input("\nPress ENTER to Close the Program...")

# But in The End, The Temporary File should be Removed, Which is done By the remove function from the OS module imported UP THERE.
remove("key")