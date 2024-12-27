from pypresence import Presence
import time
import dotenv
import os
import requests

dotenv.load_dotenv() # load from the .env

API_KEY = os.getenv("APIKEY")
client_id = os.getenv("CLIENTID")
username = os.getenv("USERNAME")
use_skycrypt = os.getenv("SKYCRYPT")
always_skycrypt = os.getenv("ALWAYS_SKYCRYPT")
forums_profile = os.getenv("FORUMS_PROFILE")
print(always_skycrypt==True)
UUID = response = requests.get(f"https://api.mojang.com/users/profiles/minecraft/{username}").json()["id"] # uses the magic api to get your uuid

headers = {"API-Key":API_KEY}

RPC = Presence(client_id)  # make the rpc exist
RPC.connect() # make the rpc do the thing

gamenames = requests.get("https://api.hypixel.net/v2/resources/games", headers=headers).json() # gets all the names of games and modes

icons = { # this is every game ever made for every platform ever
    "BEDWARS": "bedwars",
    "QUAKECRAFT": "quakecraft",
    "BUILD_BATTLE": "buildbattle",
    "UHC":"uhc",
    "SKYBLOCK":"skyblock",
    "HOUSING":"housing",
    "MCGO":"cvc",
    "SURVIVAL_GAMES":"sg",
    "BATTLEGROUNDS":"warlords",
    "MURDER_MYSTERY":"murdermystery",
    "ARCADE":"arcade",
    "ARENA":"arena",
    "TNTGAMES":"tnt",
    "WALLS":"walls",
    "SKYWARS":"skywars",
    "VAMPIREZ":"vampirez",
    "WALLS3":"megawalls", # walls3 my favourite gaming event
    "PAINTBALL":"paintball",
    "SUPER_SMASH":"smashheroes",
    "SMP":"smp",
    "PIT":"pit",
    "SPEED_UHC":"uhc", # idk and idc if/where the speed uhc icon is
    "DUELS":"duels",
    "GINGERBREAD":"turbokartracing", # WHY is it called gingerbread???
}

while True:  # the presence runs while the program runs
    useractivity = requests.get(f"https://api.hypixel.net/v2/status?uuid={UUID}", headers=headers).json() # all of this is basically copy-pasted from lobsterbot
    print(useractivity)
    if useractivity["session"]["online"] == True:
        userGame = useractivity["session"]["gameType"]
        prettifiedGame = gamenames["games"][userGame]["name"]
        try:

            userMode = useractivity["session"]["mode"]
            if userMode == "LOBBY":
                prettifiedMode = "In Lobby"
            else:
                prettifiedMode = gamenames["games"][userGame]["modeNames"][userMode]
            try:
                usermap = useractivity["session"]["map"]
                matchdetails = f"{prettifiedMode} on {usermap}"
            except:
                matchdetails = prettifiedMode
        except:
            matchdetails = None
        if userGame in icons:
            icon = icons[userGame]
            print(f"Icon: {icon}")
        else:
            icon = None
            print("No icon found")
        buttons = []
        if not (forums_profile == None):
            buttons = [{"label":"Forums Profile", "url":f"https://hypixel.net/members/{forums_profile}/"}]
        
        if ((use_skycrypt == True) and (userGame == "SKYBLOCK")) or always_skycrypt == True:
            buttons.append({"label": "Skycrypt Profile", "url": f"https://sky.shiiyu.moe/stats/{username}"})
        if buttons == []:
            buttons = None
        print(RPC.update(state=matchdetails,details=prettifiedGame,large_image=icon,buttons=buttons))
    else:
        print("User not online")
        RPC.clear()
    time.sleep(15) # thanks to ratelimits, it only updates every 15 seconds