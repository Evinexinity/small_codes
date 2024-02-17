from wifi_pass import *
from time import sleep

name = input("Enter Device Name:\n>>> ")
name = name.lower()
if name == "all":
    print(get_all_known_passwords())
    sleep(10)
else:
    print(get_password(name=name))
    sleep(10)