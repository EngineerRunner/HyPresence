# HyPresence - Discord Rich Presence for Hypixel  
[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)  
Change your Discord rich presence to the game you're playing on Hypixel!  
  
![Bedwars rich presence](/media/bedwars.png) ![Duels rich presence](/media/duels.png) ![Replay rich presence](/media/replay.png)  
![Skyblock rich presence](/media/skyblock.png) ![TNT rich presence](/media/tnt.png) ![Skywars](/media/skywars.png)
## Usage  
1. Download and extract the latest release, rename `.env.example` to `.env` and add your Minecraft username
2. Install `pypresence`, `requests` and `dotenv` with the command `pip install pypresence requests python-dotenv`  
3. Obtain a Hypixel API key, and add it to the .env
> An API key can be obtained by going to https://developer.hypixel.net/dashboard/ and clicking "Create API Key". By doing so, users can generate an API key that comes with a default rate limit of 300 requests per 5 minutes, but will expire in 72 hours (3 days). To obtain a permanent key, you must click "Create App" and select "Personal API Key", which will grant you a key that provides the same default rate limit, but will not expire on its own.
4. Optional: In the .env, enable linking your profile on Skycrypt and/or your Hypixel Forums profile (details are in the .env.example)
5. Run the script and hope it works

## Notes
- Discord must be open for it to appear
- The script must be running for it to appear
- **NEVER** share your `.env`, especially your Hypixel API key
- Your "Online Status" must be enabled in your API settings on Hypixel

## Credits
Thanks to qwertyquerty for creating [PyPresence](https://github.com/qwertyquerty/pypresence), and to the Skyblock Wikia for the API key instructions.
