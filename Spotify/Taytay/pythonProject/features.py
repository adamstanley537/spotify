import pandas as pd
import pprint
import spotipy

df = pd.read_csv("taytracks.csv")
spotify = spotipy.oauth2.SpotifyOAuth(client_id="5a76ffc39d08462f89cc4acf4857df4a",
                                 client_secret="67db852f98f54a20a0e5c992bcd84889",
                                 redirect_uri="http://example.com")

access_code = spotify.get_access_token(as_dict=False)
sp = spotipy.Spotify(auth=access_code)

analysis=[]
for i in range(433):
    analysis.append(sp.audio_features([df["id"][i]])[0])

df_ana = pd.DataFrame(analysis)

df = pd.merge(df, df_ana, left_index=True, right_index=True)

df.to_csv("taydata.csv")