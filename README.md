# Play and Stream torrent files in VLC - Windows 

### Shout out
This project is inspired from Bugs Writer [notflix](https://github.com/bugswriter/notflix).  
He used bash scripting, so it only run on Linux based system. 

So this project is totally wriiten for Windows users in Python Language


### How does this work?

This is a python script. It scape 1337x and get the magnet link.
After this it use [peerflix](https://github.com/mafintosh/peerflix) to stream the video from magnet link.
For scraping script use python http.client, sys, time libraries, re.


## Dependencies

1. node.js
1. peerflix
1. VLC


### to install dependencies:

1.  [Click](https://nodejs.org/dist/v16.15.0/node-v16.15.0-x64.msi) to download NodeJS installer

1.  Install NodeJS by executing the .msi file

1.  Click Start and open NodeJS Command Prompt and type<p>
    ```npm install -g peerflix ```

1.  [Click](https://mirrors.estointernet.in/videolan/vlc/3.0.3/win64/vlc-3.0.3-win64.exe) to download VLC Player and install it.


## How to run

> Watch the video on how to run [video]()

- Clone or download this repo. 
- Open Terminal or PowerShell or Command Prompt in the repo folder.
- To run the script :
    - Run the ```search-final.py``` file
    - Enter the name to be searched
        - eg. ```Enter name : avatar 2009```

- Select the file from drop down. 
    - Hint : Select the top ones since they have more seeders.

- That's it. Your searched file will be play in the VLC player.
