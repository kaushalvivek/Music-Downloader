''' 
Configuration File for Linux Machines running debain
to run the Application musicdownloader.py

'''


import os

# For updating the system
os.system ('sudo apt update')

# For installation of pip3
os.system ('sudo apt install python3-pip')

# For installation of Youtube - Downloader
os.system ('sudo pip3 install youtube-dl')

# For installation of BeautfulSoup4
os.system ('sudo apt install python3-bs4')
print("*"*100)
print("\t\tCongrats! Your machine is now configured for musicdownloader.")
print("*"*100)
exit()
