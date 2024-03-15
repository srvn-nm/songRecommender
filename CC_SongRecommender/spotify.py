import requests


# noinspection PyCompatibility
def get_spotify_recommendations(spotify_song_ids, artists_ids, genre_ids):
    # This function assumes you have obtained an access token from Spotify
    url = "https://spotify23.p.rapidapi.com/recommendations/"
    headers = {
        "X-RapidAPI-Key": "4f572370c6mshea36af5374dcaa6p10e8ddjsn40a8eb8b2bf2",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }
    querystring = {"limit": "20", "seed_tracks": str(spotify_song_ids), "seed_artists": str(artists_ids),
                   "seed_genres": str(genre_ids)}

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()


def search_spotify_song_id(song_name):
    url = "https://spotify23.p.rapidapi.com/search/"

    querystring = {"q": song_name, "type": "tracks", "offset": "0", "limit": "1", "numberOfTopResults": "10"}

    headers = {
        "X-RapidAPI-Key": "4f572370c6mshea36af5374dcaa6p10e8ddjsn40a8eb8b2bf2",
        "X-RapidAPI-Host": "spotify23.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring).json().get("tracks", {}).get("items", [])

    if response:
        return response[0].get("id")
    else:
        return None
