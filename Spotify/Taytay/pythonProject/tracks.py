import spotipy
import pprint
import pandas as pd

spotify = spotipy.oauth2.SpotifyOAuth(client_id="5a76ffc39d08462f89cc4acf4857df4a",
                                 client_secret="67db852f98f54a20a0e5c992bcd84889",
                                 redirect_uri="http://example.com")

access_code = spotify.get_access_token(as_dict=False)

sp = spotipy.Spotify(auth=access_code)

artist = "Taylor Swift"
search = sp.search(q='artist:' + artist, type='artist')
artist_id = search["artists"]["items"][0]["id"]

results = sp.artist_albums(artist_id=artist_id)
pprint.pprint(results["items"][0])

album_list = []
for album in results["items"]:
    album_item = {
        "name": album["name"],
        "id": album["id"],
        "uri": album["uri"],
        "date": album["release_date"]
    }
    album_list.append(album_item)

# pprint.pprint(album_list)

track_list = []

df = pd.DataFrame(columns=["name","id","album","date"])


ind = 0
for album in album_list:
    tracks = sp.album_tracks(album_id=album["id"])
    for track in tracks["items"]:
        track_item = {
            "name": track["name"],
            "id": track["id"],
            "album": album["name"],
            "date": album["date"]
        }
        track_list.append(track_item)
        df.loc[ind] = [track["name"], track["id"], album["name"], album["date"]]
        ind += 1

df.to_csv("taytracks.csv")
