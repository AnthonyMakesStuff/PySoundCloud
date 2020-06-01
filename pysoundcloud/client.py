import re
import requests

from typing import Union

from pysoundcloud.soundcloudplaylists import SoundCloudPlaylists
from pysoundcloud.soundcloudsearchresults import SoundCloudSearchResults
from pysoundcloud.soundcloudlikedtracks import SoundCloudLikedTracks
from pysoundcloud.soundcloudplaylist import SoundCloudPlaylist
from pysoundcloud.soundcloudtrack import SoundCloudTrack
from pysoundcloud.soundcloudrelatedtracks import SoundCloudRelatedTracks


class Client:
    base_url = "https://api-v2.soundcloud.com/"

    def __init__(self, client_id: str) -> None:
        """
        Setup the SoundCloud client to interact with the API

        :param client_id: Your SoundCloud client ID
        :return: None
        """
        self.client_id = client_id

    def search(self,
               query: str,
               limit: int = 10,
               offset: int = 0) -> Union[bool, SoundCloudSearchResults]:
        """
        Search SoundCloud for the specified query
        For some reason it doesn't always work and I have no clue why

        :param query: The query to search for
        :param limit: The number of results to return
        :param offset: The start position from 0
        :return: SoundCloudSearchResults, or False if response is not 200
        """
        parameters = {"q": query,
                      "limit": limit,
                      "offset": offset,
                      "client_id": self.client_id}
        url = self.base_url + "search"
        response = requests.get(url, params=parameters)
        if (response.status_code != 200):
            print("Error: Received code {}".format(response.status_code))
            return False

        return SoundCloudSearchResults(response, client_id=self.client_id, parent=self)

    def track(self, track_id: int) -> Union[bool, SoundCloudTrack]:
        """
        Gets data about the track with the specified track_id

        :param track_id: The track id to search for
        :return: a SoundCloudTrack with data about the track, or False if response is not 200
        """
        parameters = {"client_id": self.client_id}
        url = self.base_url + "tracks/{}".format(track_id)
        response = requests.get(url, params=parameters)
        if (response.status_code != 200):
            print("Error: Received code {}".format(response.status_code))
            return False
        return SoundCloudTrack(response.json(), self.client_id, parent=self)

    def related(self, track_id: int, limit: int = 10, offset: int = 0) -> Union[bool, SoundCloudRelatedTracks]:
        """
        Gets tracks related to the specified track_id

        :param track_id: The track id to find related tracks for
        :param limit: The number of tracks to find
        :param offset: The number of tracks to search for from zero, so offset 10 and limit 10 means find tracks 10-20
        :return: SoundCloudRelatedTracks with the tracks, or False if response is not 200
        """
        parameters = {"limit": limit,
                      "offset": offset,
                      "client_id": self.client_id}
        url = self.base_url + "tracks/{}/related".format(track_id)
        response = requests.get(url, params=parameters)
        if (response.status_code != 200):
            print("Error: Received code {}".format(response.status_code))
            return False
        return SoundCloudRelatedTracks(response.json(), self.client_id)

    def playlists(self,
                  track_id: int,
                  representation: str = "mini",
                  limit: int = 10,
                  offset: int = 0) -> Union[bool, SoundCloudPlaylists]:
        """
        Gets playlists containing a specified track

        :param track_id: The track ID to find playlists containing
        :param representation: The type of representation (either full or mini)
        :param limit: The number of results to return
        :param offset: The start position from 0
        :return: SoundCloudPlaylists containing the track, or False if response is not 200
        """
        parameters = {"representation": representation,
                      "limit": limit,
                      "offset": offset,
                      "client_id": self.client_id}
        url = self.base_url + "tracks/{}/playlists_without_albums".format(track_id)
        response = requests.get(url, params=parameters)
        if (response.status_code != 200):
            print("Error: Received code {}".format(response.status_code))
            return False
        return SoundCloudPlaylists(response.json(), self.client_id, parent=self)

    def albums(self,
               track_id: int,
               representation: str = "mini",
               limit: int = 10,
               offset: int = 0) -> Union[bool, SoundCloudPlaylists]:
        """
        Gets albums containing a specified track

        :param track_id: The track ID to find albums containing
        :param representation: The type of representation (either full or mini)
        :param limit: The number of results to return
        :param offset: The start position from 0
        :return: SoundCloudPlaylists containing the track, or False if response is not 200
        """
        parameters = {"representation": representation,
                      "limit": limit,
                      "offset": offset,
                      "client_id": self.client_id}
        url = self.base_url + "tracks/{}/albums".format(track_id)
        response = requests.get(url, params=parameters)
        if (response.status_code != 200):
            print("Error: Received code {}".format(response.status_code))
            return False
        if (len(response.json()["collection"]) == 0):
            return False
        return SoundCloudPlaylists(response.json(), self.client_id)

    def comments(self):
        pass  # Todo: add comments

    def web_profiles(self):
        pass  # Todo: add web_profiles

    def liked_tracks(self,
                     user_id: int,
                     limit: int = 24,
                     offset: int = 0) -> Union[bool, SoundCloudLikedTracks]:
        """
        Gets the user's liked tracks

        :param user_id: The ID of the user to find liked tracks for
        :param limit: The number of results to return
        :param offset: The start position from 0
        :return: SoundCloudLikedTracks containing all the tracks, or False if response is not 200
        """
        parameters = {"client_id": self.client_id,
                      "limit": limit,
                      "offset": offset}
        url = self.base_url + "users/{}/track_likes".format(user_id)
        response = requests.get(url, params=parameters)
        if (response.status_code != 200):
            print("Error: Received code {}".format(response.status_code))
            return False

        return SoundCloudLikedTracks(response, client_id=self.client_id)

    def playlist(self,
                 playlist_id: int = None,
                 playlist_url: str = None,
                 representation: str = "full",
                 secret_token: str = None) -> Union[bool, SoundCloudPlaylist]:
        """
        Get a playlist based on a specified playlist_id or playlist_url

        :param playlist_id: The ID of the playlist
        :param playlist_url: The URL of the playlist
        :param representation: The playlist representation (either fill or mini)
        :param secret_token: An optional secret token
        :return: A SoundCloudPlaylist, or False if response is not 200
        """
        if (playlist_id is None):
            if (playlist_url is not None):
                response = requests.get(playlist_url)
                patterns = [
                    r'<meta property="twitter:app:url:(?:googleplay|iphone|ipad)'
                    r'content="soundcloud:\/\/playlists:([0-9]+)">',
                    r'<meta property="twitter:player" content="https:\/\/w\.soundcloud\.com\/player\/\?url=https'
                    r'%3(?:a|A)%2(?:f|F)%2(?:f|F)api\.soundcloud\.com%2(?:f|F)playlists%2(?:f|F)([0-9]+)',
                    r'<meta property="al:(?:ios|android):url" content="soundcloud:\/\/playlists:([0-9]+)">',
                    r'<link rel="alternate" href="android-app:\/\/com\.soundcloud\.android\/soundcloud\/'
                    r'playlists:([0-9]+)">',
                    r'<link rel="alternate" href="ios-app:\/\/336353151\/soundcloud\/playlists:([0-9]+)">'
                ]

                for pattern in patterns:
                    if (playlist_id is None):
                        search_results = re.search(pattern,
                                                   response.text)
                        if (search_results is not None):
                            playlist_id = search_results.group(1)
        if (playlist_id is None):
            print("Error: Could not find the playlist id from the url \"{}\"".format(playlist_url))
            return False

        parameters = {"representation": representation,
                      "client_id": self.client_id}
        if (secret_token is not None):
            parameters["secret_token"] = secret_token
        url = self.base_url + "playlists/{}".format(playlist_id)
        response = requests.get(url, params=parameters)
        if (response.status_code != 200):
            print("Error: Received code {}".format(response.status_code))
            return False
        return SoundCloudPlaylist(response.json(),
                                  self.client_id,
                                  parent=self)
