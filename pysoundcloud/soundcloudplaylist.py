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

    """
    :var duration: [SC] Duration in milliseconds
    :var permalink_url: [SC] URL to the SoundCloud.com page
    :var reposts_count: The number of reposts for the playlist
    :var genre: [SC] The genre of the playlist
    :var permalink: [SC] Permalink of the resource
    :var purchase_url: [SC] External purchase link
    :var description: [SC] HTML description
    :var uri: [SC] API resource URL
    :var label_name: [SC] Label name
    :var set_type: (Honestly, no clue -- please someone help me)
    :var public: Is the playlist public
    :var track_count: [SC] Number of public tracks
    :var user_id: [SC] User ID of the owner
    :var last_modified: The timestamp the playlist was last modified
    :var license: [SC] Creative common license
    :var tracks: All the tracks in the playlist
    :var id: The ID of the playlist
    :var release_date: (I also don't know what this is. Maybe the timestamp the playlist was created?)
    :var display_date: (I really have no idea what this is)
    :var sharing: [SC] Public/private sharing
    :var created_at: [SC] timestamp of creation
    :var likes_count: The number of likes the playlist has
    :var title: The title of the playlist
    :var purchase_title: (No clue, and apparently SoundCloud doesn't know either from their API documentation)
    :var managed_by_feeds: (Also not sure, but I guess it says whether or not the playlist is managed by an RSS feed?)
    :var artwork_url: The URL for the artwork for the playlist
    :var is_album: True if the playlist is an album, false if it is just a playlist
    :var user: A SoundCloudUser with the details of the user
    :var published_at: (Same as created at? Maybe it's when a private playlist went public?)
    :var embeddable_by: [SC] Who can embed this track or playlist ["all", "me", "none"]
    """

    def __init__(self, data: dict, client_id: str = None, album: bool = False, parent=None) -> None:
        """
        :param data: The json dict from the response
        :param client_id: The ID of the client
        :param album: Is the playlist actually an album
        :param parent:
        """
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
