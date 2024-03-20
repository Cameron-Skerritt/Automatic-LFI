# Automatic Local File Inclusion Script

This script is an automatic tool for CTFs which try's basic LFI, RFI and RCE methods.
This is just a PoC. This is inspired from: fimap, an old, outdated LFI script.
fimap: https://github.com/kurobeats/fimap

## Current Functionality
- Basic Local File Inclusion Enumeration
- Remote Shell capabilities
- Fully automatic (requires local python server for RFI & nc server)


## How to use it?
1) Simply download the .py file & rfI_test.php file.
2) Edit the attacker_ip & port to your local IP & listener port. (python server is defaulted to port 80.)
3) python3 alfi.py
4) Enter vulnerable URL. i.e. "http://10.10.10.10/search.php?page="
And off it goes! :)
![image](https://github.com/Cameron-Skerritt/Automatic-LFI/assets/122690042/962f65bd-859b-4a08-9b3e-8315f88db74b)


Note: The script will display the URL it found which is vulnerable.
When giving a vulnerable URL, include the full vulnerable URL including http.

## Why did you create this?
This is merely a side project of mine, I wanted to have an automatic tool that try's all LFI possabilities to speed things up when doing CTFs, however, since fimap is no longer maintained, I decided to create my own version.
This isn't overly complicated but a PoC at best.
I do intend on making it more complex by adding RFI, encoding, more shells in case the main one doesn't work etc.

# To Do List
1) Show current location if possible.
2) Fix PHP Wrappers (Currently broken)
3) Add encoding for each list with varying complexity.
4) automatically detect the vulnerable part of the URL
