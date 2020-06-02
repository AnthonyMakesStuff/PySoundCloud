from typing import List

from pysoundcloud.soundcloudplaylist import SoundCloudPlaylist


class SoundCloudPlaylists:
    playlists: List[SoundCloudPlaylist] = None
    next_href: str = ""
    query_urn: str = ""

    """
    :var playlists: The playlists
    :var next_href: The URL for the next page of results
    :var query_urn: The API resource URL for this query
    """

    def __init__(self, data: dict, client_id: str = None, albums: bool = False, parent=None):
        """
        :param data: The json dict from the response
        :param client_id: The ID of the client
        :param albums: Are the playlists albums
        :param parent:
        """
        self.index = 0
        self.playlists = list()
        self.next_href = data["next_href"]
        self.query_urn = data["query_urn"]
        for playlist in data["collection"]:
            self.playlists.append(SoundCloudPlaylist(playlist, client_id, albums, parent=parent))

    def __iter__(self):
        return self

    def __next__(self) -> SoundCloudPlaylist:
        try:
            value = self.playlists[self.index]
            self.index += 1
            return value
        except IndexError:
            raise StopIteration

    def __getitem__(self, item):
        return self.playlists[item]
