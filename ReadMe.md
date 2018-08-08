Music Downloader
===================

Because Downloading Music is too much of a hassle nowadays. <br />
***Version***: *2.0* <br />
***Release***: *18-10-2017* <br />
***Author***: *Vivek Kaushal* <br />

http://vivekkaushal.com/
<br>

This **README** file contains :
 1. [About](#about)
 2. [Requirements](#requirements)
 3. [Installation Instructions](#installation-instructions)
 4. [Usage Instructions](#usage-instructions)
 5. [Terms and Conditions](#terms-and-conditions)
 

----------


About
--------

>**MusicDownloader** is a product born out of necessity. Though the streaming services nowadays are pretty awesome, there are times when you just need the song. Old-fashioned way. On your machine. Or you need information about a new artist you have just been introduced to. This product solves that problem, by making downloading songs as easy as it gets. No more scrambling with scams and adware on mp3 download sites. <br />
>Hope you like it!


----------


Requirements
------------

#### For Mac: 

- Homebrew<br>
Run this code in your terminal:
```
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```
- Python3<br>
Run this code in your ternimal:
```
brew update
brew install python3
```

#### For Linux:

- Python3<br>
Run this code in your terminal:
```
sudo apt-get update
sudo apt-get install python3
```

------------------------

Installation Instructions
--------------------------
#### For Mac:<br />
Once the Requirements have been satisfied, use the ***mac_config.py*** configuration file to set your system up for **MusicDownoader**.

Run The Following Code in your Terminal:
```
python3 mac_config.py
```
This will return your installation status. Proceed with Usage Instructions.

#### For Linux: <br />
Once the Requirements have been satisfied, use the ***linux_config.py*** configuration file to set your system up for **MusicDownoader**.

Run The Following Code in your Terminal:
```
python3 linux_config.py
```
This will return your installation status. Proceed with Usage Instructions.
__________________

Usage Instructions
------------------
Once the installation instructions have been followed, run the following code in your terminal to launch the application:
```
python3 music_downloader.py
```
Now, specify the song and artist, as show in the example below:
```
Enter Artist's Name:
Coldplay
```
Choose if you want to see suggestions for songs by this artist:
```
Do you want song suggestions? (Y/n) Y
```

A list of the Artist's best songs will be displayed if you choose to see it for your reference, your download choice though is ***not limited*** to this list. You can choose to download ***any song by the artist***.

PS: The 'Suggestions' is in Beta. It might yield buggy results.
```
Enter Song's Name:
Fix You
```
Please note, that you need not be perfect with your input, the program is capable of dealing with simple typos.

Once the download completes the following will be displayed:
```
Song Downloaded!
Stored in Downloads Folder.
Enter the following Options to move ahead:
'A' - to download another song by the same artist
'B' - to download another song by a different artist
'Q' - to quit
```
Choose the option you wish to choose and proceed. Press 'Q' or 'q' to quit, and the exit screen will be displayed.
```
Thanks for using!
Checkout www.vivekkaushal.com for more such stuff.
```
Contact vivek.kaushal@outlook.com for help with usage.
___________________

Terms and Conditions
--------------------
This application is for educational purpose only, and I do no condone the download or distribution of illegal music. I do not take responsibility of what you choose to do with this application. The code is distributed under the **MIT License.**
_______________

For more such stuff, visit http://vivekkaushal.com.


----------
