import requests
import pandas as pd

head = {

    'Authorization': 'Bearer z7y7adz7u62v11sonxteun0r0uhep9',
    'Client-Id': 'vlxltq3gqppxz5dbzbjvn5fco0qikf'''

}

# https://dev.twitch.tv/docs/api/reference#get-videos
# api gives id, stream_id, user_id, user_login, user_name, title, description, created_at, published_at, url, thumbnail_url, viewable, view_count, language, type, duration, muted_segments and pagination

streamers = []

def name(streamer, playing):

    stream = requests.get('https://api.twitch.tv/helix/videos?id='+streamer, headers=head)

    data = stream.json()

    df = pd.DataFrame(data["data"])
    df["games"] = playing
    df.pop("id") 
    df.pop("stream_id")
    df.pop("user_id")
    df.pop("user_login")

    streamers.append(df)

# Top 100
# Males: (took the latest video from 8nov, otherwise from before, and collected the data. Did not include companies)
# (had to write the games myself, because webscraping on Twitch did not work (the website is too fluid i found in forumns) so i looked at the game tag and wrote it down)
# (females are in other py)
name("1200148484", "Variety (5+ of games)")
name("1199835516", "War by Grow Games")
name("1199666252", "Minecraft")
name("1199862122", "Just Chatting")
name("1200045448", "Grand Theft Auto")
name("1200068177", "iRacing")
name("1199868985", "Apex Legends")
name("1199809799", "Just Chatting")
name("1195952776", "Apex Legends")
name("1200117091", "League of Legends")

name("1197612994", "League of Legends")
name("1193860723", "Minecraft")
name("1199505338", "Valorant")
name("1197948807", "Just Chatting")
name("1200102007", "Variety (5+ of games)")
name("1199722191", "Counter-Strike")
name("1199489485", "Minecraft")
name("1199857575", "Variety (5+ of games)")
name("1199779541", "Slots")
name("1200077506", "Lost Ark")

name("1199626294", "Just Chatting")
name("1161563090", "New World")
name("1192286277", "League of Legends")
name("1199820459", "Grand Theft Auto")
name("1194098217", "Dead by Daylight")
name("1197619598", "League of Legends")
name("1023582456", "Just Chatting")
name("1200248836", "Just Chatting")
name("1197290588", "Slots")
name("1199919639", "Just Chatting")

name("1198648216", "Valorant")
name("1157913755", "Dota 2")
name("1199823161", "Grand Theft Auto")
name("1199884897", "Escape from Tarkov")
name("1199716963", "Variety (5+ of games)")
name("1198635565", "Variety (5+ of games)")
name("1199490466", "Variety (5+ of games)")
name("1199040401", "Just Chatting")
name("1199786701", "Call of Duty")
name("1199919639", "Just Chatting")

name("1199654807", "FIFA 22")
name("1198056179", "Variety (5+ of games)")
name("1199607211", "Lost Ark")
name("1196936827", "League of Legends")
name("1199674977", "Apex Legends")
name("1199413549", "Lost Ark")
name("1198224154", "Just Chatting")
name("1200034388", "Mount & Blafe II: Bannerlord")
name("1200040841", "Final Fantasy XIV Online")
name("1199844602", "Apex Legends")

name("1191251082", "Minecraft")
name("1199099276", "Apex Legends")
name("1199639837", "Minecraft")
name("1199881082", "Grand Theft Auto")
name("1200129704", "Call of Duty")
name("1191398339", "Variety (5+ of games)")
name("1199108989", "League of Legends")
name("1199810239", "Call of Duty")
name("1199742169", "Escape from Tarkov")
name("1200057642", "Variety (5+ of games)")

name("1199872782", "Variety (5+ of games)")
name("1199798669", "League of Legends")
name("1199545572", "Call of Duty")
name("1199407019", "Call of Duty")
name("1199761592", "Variety (5+ of games)")
name("1199757677", "Minecraft")
name("1199635395", "Dota 2")
name("1199639180", "Dota 2")
name("1199639069", "Chess")
name("1191509432", "Just Chatting")

name("1199272045", "Just Chatting")
name("1200010922", "Fortnite")
name("1197622549", "League of Legends")
name("1200123384", "SMITE")
name("1199796080", "Darkest Dungeon II")
name("1199533593", "Hearthstone")
name("1200188572", "Just Chatting")
name("1199587012", "Call of Duty")
name("1198667841", "Apex Legends")
name("1199963994", "Brawlhalla")

name("1200253901", "Variety (5+ of games)")
name("1199873628", "FIFA 22")
name("1199828781", "FIFA 22")
name("1192020129", "League of Legends")
name("1199775301", "Just Chatting")
name("1197197311", "Just Chatting")
name("1196525503", "League of Legends")
name("1199763312", "Grand Theft Auto")
name("1198864501", "Lost Ark")
name("1199593784", "Lost Ark")

name("1199431254", "Variety (5+ of games)")
name("1199753996", "Fortnite")
name("1199861154", "Variety (5+ of games)")
name("1199608778", "Variety (5+ of games)")
name("1192601942", "Valorant")
name("1199780094", "FIFA 22")
name("1199758483", "Call of Duty")
name("1199761135", "Minecraft")

#females
#name("1141769391", "Hot Tub streams")
#name("1195880574", "Valorant")

merged = pd.concat(streamers).reset_index()
