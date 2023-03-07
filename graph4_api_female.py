import requests
import pandas as pd

head = {

    'Authorization': 'Bearer dwjc8k3gk5r1mixidz55u5bnl9sv38',
    'Client-Id': 'vlxltq3gqppxz5dbzbjvn5fco0qikf'''

}

streamers_female = []

def name(streamer, playing):

    stream = requests.get('https://api.twitch.tv/helix/videos?id='+streamer, headers=head)

    data = stream.json()

    df = pd.DataFrame(data["data"])
    df["games"] = playing
    df.pop("id") 
    df.pop("stream_id")
    df.pop("user_id")
    df.pop("user_login")

    streamers_female.append(df)

# Top 100
# Females
name("1141769391", "Hot Tub streams")
name("1195880574", "Valorant")

merged2 = pd.concat(streamers_female).reset_index()
