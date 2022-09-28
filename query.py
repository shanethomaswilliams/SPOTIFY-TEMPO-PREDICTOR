import requests
import get_token


def valid_token():
    token = get_token.get_token()
    if token[0:8] == "Error: ":
        return 0
    else:
        return token


def run_search_query(param_dict):
    token = valid_token()
    url = 'https://api.spotify.com/v1/search'
    auth_header = {'authorization': 'Bearer ' + token}
    response = requests.get(url, headers=auth_header, params=param_dict)
    return response


def run_simple_query(url):
    token = valid_token()
    auth_header = {'authorization': 'Bearer ' + token}
    response = requests.get(url, headers=auth_header)
    return response


def get_audio_features(spotify_id):
    return run_simple_query('https://api.spotify.com/v1/audio-features/'
                            + spotify_id)


def get_full_album(spotify_id):
    return run_simple_query('https://api.spotify.com/v1/albums/'
                            + spotify_id)


# len(spotify_ids) <= 20
def get_full_albums(spotify_ids):
    url_ids = '?ids='
    for album_id in spotify_ids:
        url_ids += album_id + ','
    url_ids = url_ids[:-1]
    result = run_simple_query('https://api.spotify.com/v1/albums/'
                              + url_ids)
    return result.json()['albums']


def get_artist(spotify_id):
    return run_simple_query('https://api.spotify.com/v1/artists/'
                            + spotify_id)


def get_track(spotify_id):
    return run_simple_query('https://api.spotify.com/v1/tracks/'
                            + spotify_id)


def get_tracks(spotify_ids):
    result = list()
    while len(spotify_ids) > 0:
        if len(spotify_ids) >= 50:
            current_ids = spotify_ids[0:50]
            spotify_ids = spotify_ids[50:]
        else:
            current_ids = spotify_ids
            spotify_ids = []
        url_ids = '?ids='
        for spotify_id in current_ids:
            url_ids += spotify_id + ','
        url_ids = url_ids[:-1]
        tracks = run_simple_query('https://api.spotify.com/v1/tracks/'
                                  + url_ids)
        tracks = tracks.json()['tracks']
        features = run_simple_query('https://api.spotify.com/v1/audio-features/'
                                    + url_ids)
        features = features.json()['audio_features']
        for i in range(0, len(tracks)):
            result.append([tracks[i], features[i]])
    return result
