import random, string, requests, time
from colorama import Fore, Style
import concurrent.futures
import os

# User selection for the platform
def get_user_choice():
    print(Fore.WHITE + """
        [1] Tiktok                 [6] Fortnite      
        [2] SoundCloud             [7] Telegram
        [3] Medal                  [8] Instagram
        [4] Steam                  [9] Spotify
        [5] Twitch                 [10] Youtube

        [99] Custom link
    """)
    try:
        K4 = int(input(Fore.WHITE + "Choose one: "))
        if K4 not in range(1, 11) and K4 != 99:
            print(Fore.RED + "Invalid selection! Please choose a number between 1-10 or 99 for a custom link.")
            return get_user_choice()  # Recursively ask again for valid input
        return K4
    except ValueError:
        print(Fore.RED + "Please enter a valid number.")
        return get_user_choice()

K4 = get_user_choice()

# Mapping platforms to URLs
platforms = {
    1: ('tiktok.com/@', "Tiktok"),
    2: ('soundcloud.com/', "SoundCloud"),
    3: ('medal.tv/de/u/', "Medal"),
    4: ('https://steamcommunity.com/id/', "Steam"),
    5: ('m.twitch.tv/', "Twitch"),
    6: ('fortnitetracker.com/profile/search?q=', "Fortnite"),
    7: ('web.telegram.org/k/#@', "Telegram"),
    8: ('instagram.com/', "Instagram"),
    9: ('open.spotify.com/user/', "Spotify"),
    10: ('www.youtube.com/@', "Youtube"),
}

# If custom link is selected, ask the user to input it
if K4 == 99:
    webss = input(Fore.WHITE + "Enter the custom link prefix (e.g., 'example.com/@'): ")
    webs = "Custom Link"
else:
    webss, webs = platforms[K4]

def check(users): 
    try:
        r = requests.get(f'https://{webss}{users}')
        if r.status_code == 200:
            print(Fore.WHITE + "[+] " + Fore.RED + "Taken" + Fore.WHITE + f' {users}')
        else:
            print(Fore.WHITE + "[+] " + Fore.GREEN + "Available" + Fore.WHITE + f' {users}')
            with open("Hits.txt", "a", encoding='utf-8') as f:
                f.write(f"{users} | Available or Banned On => {webs} |\n")
    except requests.exceptions.RequestException as e:
        print(Fore.YELLOW + f"Error checking {users}: {e}")
        pass

# Reading users from the file and checking availability
def check_usernames():
    with open('users.txt', 'r') as f:
        users = [line.strip() for line in f]
    
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.map(check, users)

if __name__ == "__main__":
    check_usernames()
