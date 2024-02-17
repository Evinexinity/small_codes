from subprocess import getoutput
import wifiPassword

def get_password(name):
    """Asks For The Target Wi-Fi Name, And Gives The Desired Wi-Fi Password As An Output."""
    password = getoutput(f"wifiPassword {name}")
    return password

def wifi_list():
    """Returns a List Of Wi-Fi(s) That The Machine Has Connected To."""
    wifi_list_unmanaged = getoutput("netsh wlan show profile").replace("Profiles on interface Wi-Fi:", "").replace("Group policy profiles (read only)", "").replace("---------------------------------", "").replace("User profiles", "").replace("-------------", "").replace("All User Profile     :", "").replace("<None>", "").split("\n")
    wifi_list = [val for val in wifi_list_unmanaged if val != ""]                
    return wifi_list

def write_to_file():
    """Writes wifi_list to a File (optional)"""
    with open("wifi_list.txt", "w") as file:
        for line in wifi_list():
            file.write(line)

def get_all_known_passwords():
    """Gets The Password of Every Known Device To Machine."""
    for index in range(len(wifi_list())):
        print(get_password(wifi_list()[index]))