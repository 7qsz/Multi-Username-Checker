import random, string, requests, time
from colorama import Fore, Style
import concurrent.futures
import os

import fade 

print(fade.fire("""
                       
██╗   ██╗███████╗███████╗██████╗ ███╗   ██╗ █████╗ ███╗   ███╗███████╗
██║   ██║██╔════╝██╔════╝██╔══██╗████╗  ██║██╔══██╗████╗ ████║██╔════╝
██║   ██║███████╗█████╗  ██████╔╝██╔██╗ ██║███████║██╔████╔██║█████╗  
██║   ██║╚════██║██╔══╝  ██╔══██╗██║╚██╗██║██╔══██║██║╚██╔╝██║██╔══╝  
╚██████╔╝███████║███████╗██║  ██║██║ ╚████║██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
                                                                      

"""))

Title = "MULTI-PLATFORM CHECKER"
print(Title)
print("v1 | @rxyuhq ")
time.sleep(.5)

K4 = int(input(Fore.WHITE+"""
        [1] Tiktok                 [6] Fortnite      
        [2] SoundCloud             [7] Telegram
        [3] Medal                  [8] Instagram
        [4] Steam                  [9] Spotify
        [5] Twitch                 [10] Youtube

        [99] Custom link
        Choose one : """+Fore.WHITE))
webss = ''
webs = ''
if K4 == 1 :
    webss = 'tiktok.com/@'
    webs = "Tiktok"
elif K4 == 2 :
    webss = 'soundcloud.com/'
    webs = "SoundCloud"
elif K4 == 3 :
    webss = 'medal.tv/de/u/'
    webs = "Medal"
elif K4 == 4 :
    webss = 'https://steamcommunity.com/id/'
    webs = "Steam"
elif K4 == 5 :
    webss = 'm.twitch.tv/'
    webs = "Twitch"
elif K4 == 6 :
    webss = 'fortnitetracker.com/profile/search?q='
    webs = "Fortnite"
elif K4 == 7 :
    webss = 'web.telegram.org/k/#@'
    webs = "Telegram"
elif K4 == 8 :
    webss = 'instagram.com/'
    webs = "Instagram"
elif K4 == 9 :
    webss = 'open.spotify.com/user/'
    webs = "Spotify"
elif K4 == 10 :
    webss = 'www.youtube.com/@'
    webs = "Youtube"
elif K4 == 99 :
    webss = 'the link'
    webs = "name"
else:
    print('Error, please choose correct number.. ')
    time.sleep(3)
    quit()

def check(users): 
    try:
        r = requests.get(f'https://{webss}{users}')
        if r.status_code == 200:
            print(Fore.WHITE +"[+] "+Fore.RED + "Taken"+ Fore.WHITE+ f' {users}')
        else:
            print(Fore.WHITE + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + f' {users}')
            with open("Hits.txt", "a", encoding='utf-8') as f:
                f.write(f"{users} | Available or Banned On => {webs} |\n")
    except:
        pass

with open('users.txt', 'r') as f:
    users = [line.strip() for line in f]
with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(check,users)