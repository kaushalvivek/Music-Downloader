'''
A Simple Music Downloader.
Because Downloading Free Music is not as convenient as it used to be.

Vivek Kaushal
6:21 13.10.2017
'''

import os
import requests
from bs4 import BeautifulSoup

#   Stores the name of the artist if 
#   if multiple songs by the same artist
#   are being downloaded.
global_artist = ''

while(True):
    # Check for whether an artist is predefined
    if global_artist == '':
        print ("Enter Artist's Name:")
        artist = input()
        artistns = artist.replace(' ','_')
    print ("Enter Song's Name:")
    song = input()
    # Scraping YouTube for the song link
    page = requests.get("https://www.youtube.com/results?search_query="+artist+"+"+song)
    soup = BeautifulSoup(page.text,'html.parser')
    for div in soup.find_all('div', { "class" : "yt-lockup-video" }):
        if div.get("data-context-item-id") != None:
            video_id = div.get("data-context-item-id")
            break
    # Using Youtube-dl by https://github.com/rg3/youtube-dl/ for download and ffmpeg for conversion.
    os.system('youtube-dl -x --audio-format mp3 --audio-quality 0 --output "%(title)s.%(ext)s" https://www.youtube.com/watch?v='+video_id)
   
   # Storing file at <artist> in Downloads Folder
    if os.path.exists('~/Downloads/'+artistns):
        pass
    else:
        os.system("mkdir ~/Downloads/"+artistns)
    os.system("mv *.mp3 ~/Downloads/"+artistns+"/")
    print ("Song Downloaded!")
    print ("Stored in Downloads Folder.")
    print ("Enter the following Options to move ahead:")
    print ("'A' - to download another song by the same artist")
    print ("'B' - to download another song by a different artist")
    print ("'Q' - to quit\n")
    invalid_count = 0
    break_flag = 0
    while invalid_count < 5:
        if (break_flag):
            break
        continue_check = input()
        if continue_check == 'A' or continue_check == 'a':
            global_artist = artist
            break_flag+=1
            continue
        elif continue_check == 'B' or continue_check == 'b':
            global_artist = ''
            break_flag+=1
            continue
        elif continue_check == 'Q' or continue_check == 'q':
            print('\nThanks for using!')
            print('Checkout www.vivekkaushal.com for more such stuff.\n')
            exit()
        else :
            print ('Enter a valid respose [A, B, Q]')
            invalid_count+=1
    print("\nYou bored me.")
    print("Bye.")
    print('\nThanks for using!') 
    print ('Checkout www.vivekkaushal.com for more such stuff.\n')
    quit()




    


