''' 
Configuration File for Linux Machines
to run the Application musicdownloader.py

'''
import os

# For updating the system
os.system ('sudo apt-get update')

# For installation of pip3
os.system ('sudo apt-get install python3-pip')

# For installation of Youtube - Downloader
os.system ('sudo apt-get install youtube-dl')

# For installation of BeautfulSoup4
os.system ('sudo apt-get install python3-bs4')

print ("\nYour machine is now configured for musicdownloader.\n")
exit()