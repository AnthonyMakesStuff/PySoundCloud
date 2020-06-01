from contextlib import suppress
from typing import List

from pysoundcloud.soundcloudtrack import SoundCloudTrack
from pysoundcloud.soundclouduser import SoundCloudUser


class SoundCloudPlaylist:
    duration: int = 0
    permalink_url: str = ""
    # noinspection SpellCheckingInspection
    reposts_count: int = 0
    genre: str = ""
    permalink: str = ""
    purchase_url: str = ""
    description: str = ""
    uri: str = ""
    label_name: str = ""
    # Todo: add tags
    # Todo: Research set_type
    set_type: str = ""
    public: bool = False
    track_count: int = 0
    user_id: int = 0
    last_modified: str = ""
    license: str = ""
    tracks: List[SoundCloudTrack] = list()
    id: int = 0
    release_date: str = ""
    display_date: str = ""
    sharing: str = ""
    # Todo: Research secret token
    created_at: str = ""
    likes_count: int = 0
    title: str = ""
    purchase_title: str = ""
    managed_by_feeds: bool = False
    artwork_url: str = ""
    is_album: bool = False
    user: SoundCloudUser = None
    published_at: str = ""
    embeddable_by: str = ""

    def __init__(self, data: dict, client_id: str = None, album: bool = False, parent=None) -> None:
        self.duration = data["duration"]
        self.permalink_url = data["permalink_url"]
        self.reposts_count = data["reposts_count"]
        self.permalink = data["permalink"]
        self.uri = data["uri"]
        # Todo: Add tag list
        self.set_type = data["set_type"]
        self.public = data["public"]
        self.track_count = data["track_count"]
        self.user_id = data["user_id"]
        self.last_modified = data["last_modified"]
        self.tracks = []
        # The playlist only gets data for the first 5 tracks in the playlist
        # All the track IDs are stored and data for each track can be retrieved individually
        self.id = data["id"]
        self.display_date = data["display_date"]
        self.sharing = data["sharing"]
        self.created_at = data["created_at"]
        self.likes_count = data["likes_count"]
        self.title = data["title"]
        self.managed_by_feeds = data["managed_by_feeds"]
        self.artwork_url = data["artwork_url"]
        self.is_album = data["is_album"]
        self.user = SoundCloudUser(data["user"])
        self.published_at = data["published_at"]
        with suppress(KeyError):
            self.genre = data["genre"]
            self.purchase_url = data["purchase_url"]
            self.description = data["description"]
            self.label_name = data["label_name"]
            self.license = data["license"]
            for playlist_track in data["tracks"]:
                self.tracks.append(SoundCloudTrack(playlist_track,
                                                   client_id=client_id,
                                                   parent=parent))
            self.release_date = data["release_date"]
            self.purchase_title = data["purchase_title"]
            self.embeddable_by = data["embeddable_by"]

    def __str__(self) -> str:
        string_out = 'SoundCloudPlaylist(duration: {}, permalink_url: "{}", reposts_count: {}, genre: "{}", ' \
                     'permalink: "{}", purchase_url: "{}", description: "{}", uri: "{}", label_name: "{}", ' \
                     'set_type: "{}", public: {}, track_count: {}, user_id: {}, last_modified: "{}", license: "{}", ' \
                     'tracks: {}, id: {}, release_date: "{}", display_date: "{}", sharing: "{}", created_at: "{}", ' \
                     'likes_count: {}, title: "{}", purchase_title: "{}", managed_by_feeds: {}, artwork_url: "{}", ' \
                     'is_album: {}, user: {}, published_at: "{}", embeddable_by: "{}")'.format(self.duration,
                                                                                               self.permalink_url,
                                                                                               self.reposts_count,
                                                                                               self.genre,
                                                                                               self.permalink,
                                                                                               self.purchase_url,
                                                                                               self.description,
                                                                                               self.uri,
                                                                                               self.label_name,
                                                                                               self.set_type,
                                                                                               self.public,
                                                                                               self.track_count,
                                                                                               self.user_id,
                                                                                               self.last_modified,
                                                                                               self.license,
                                                                                               self.tracks,
                                                                                               self.id,
                                                                                               self.release_date,
                                                                                               self.display_date,
                                                                                               self.sharing,
                                                                                               self.created_at,
                                                                                               self.likes_count,
                                                                                               self.title,
                                                                                               self.purchase_title,
                                                                                               self.managed_by_feeds,
                                                                                               self.artwork_url,
                                                                                               self.is_album,
                                                                                               self.user,
                                                                                               self.published_at,
                                                                                               self.embeddable_by)
        return string_out

    def __repr__(self) -> str:
        return self.__str__()
