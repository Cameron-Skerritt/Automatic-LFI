# Automatic Local File Inclusion Script

This script is an automatic tool for CTFs which try's basic LFI and RCE methods.
This is just a PoC. This is inspired from: fimap, an old, outdated LFI script.
fimap: https://github.com/kurobeats/fimap


## How to use it?
1) Simply download the .py file
2) python3 script.py
3) Enter vulnerable URL. i.e. "http://10.10.10.10/search.php?page="
And off it goes! :)
![image](https://github.com/Cameron-Skerritt/Personal-Projects/assets/122690042/4b7a91a3-c7eb-4e0b-bfa8-bd773bd86f48)

Note: The script will display the URL it found which is vulnerable, when giving a vulnerable URL, include the full vulnerable URL including http.

## Why did you create this?
This is merely a side project of mine, I wanted to have an automatic tool that trys all LFI possabilities to speed things up when doing CTFs, however, since fimap is no longer maintained, I decided to create my own version.
This isn't overly complicated but a PoC at best.
I do intend on making it more complex by adding RFI, encoding, more shells incase the main one doesn't work etc.
