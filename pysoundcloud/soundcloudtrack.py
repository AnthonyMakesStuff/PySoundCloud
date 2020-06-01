from contextlib import suppress
from typing import List

from pysoundcloud.soundclouduser import SoundCloudUser
from pysoundcloud.soundcloudstream import SoundCloudStream
from pysoundcloud.soundcloudstreams import SoundCloudStreams
from pysoundcloud.trackdata import TrackData


class SoundCloudTrack:
    comment_count: int = 0
    full_duration: int = 0
    downloadable: bool = False
    created_at: str = ""
    description: str = ""
    streams: SoundCloudStreams = None
    # Todo: Add media streams
    title: str = ""
    # Todo: add publisher metadata?
    duration: int = 0
    has_downloads_left: bool = False
    artwork_url: str = ""
    public: bool = False
    streamable: bool = False
    # Todo: add tag list
    genre: str = ""
    id: int = 0
    reposts_count: int = 0
    state: str = ""
    label_name: str = ""
    last_modified: str = ""
    commentable: bool = False
    policy: str = ""
    # Todo: research visuals
    purchase_url: str = ""
    sharing: str = ""
    uri: str = ""
    # Todo: research "secret_token"
    download_count: int = 0
    likes_count: int = 0
    urn: str = ""
    license: str = ""
    purchase_title: str = ""
    display_date: str = ""
    embeddable_by: str = ""
    release_date: str = ""
    user_id: int = 0
    monetization_model: str = ""
    waveform_url: str = ""
    permalink: str = ""
    permalink_url: str = ""
    user: SoundCloudUser = None
    playback_count: int = 0
    track_index: int = -1
    album_name: str = ""

    def __init__(self,
                 data: dict,
                 client_id: str = None,
                 album_index: int = -1,
                 album_name: str = "",
                 playlist_track_index: int = -1,
                 parent=None):
        self.streams = SoundCloudStreams()
        self.id = data["id"]
        if (parent is not None):
            self.generate_album_info(parent)
        with suppress(KeyError):
            self.comment_count = data["comment_count"]
            self.full_duration = data["full_duration"]
            self.downloadable = data["downloadable"]
            self.created_at = data["created_at"]
            self.description = data["description"]
            self.title = data["title"]
            self.duration = data["duration"]
            self.has_downloads_left = data["has_downloads_left"]
            self.artwork_url = data["artwork_url"]
            self.public = data["public"]
            self.streamable = data["streamable"]
            self.genre = data["genre"]
            self.reposts_count = data["reposts_count"]
            self.state = data["state"]
            self.label_name = data["label_name"]
            self.last_modified = data["last_modified"]
            self.commentable = data["commentable"]
            self.policy = data["policy"]
            self.purchase_url = data["purchase_url"]
            self.sharing = data["sharing"]
            self.uri = data["uri"]
            self.download_count = data["download_count"]
            self.likes_count = data["likes_count"]
            self.urn = data["urn"]
            self.license = data["license"]
            self.purchase_title = data["purchase_title"]
            self.display_date = data["display_date"]
            self.embeddable_by = data["embeddable_by"]
            self.release_date = data["release_date"]
            self.user_id = data["user_id"]
            self.monetization_model = data["monetization_model"]
            self.waveform_url = data["waveform_url"]
            self.permalink = data["permalink"]
            self.permalink_url = data["permalink_url"]
            self.user = SoundCloudUser(data["user"])
            track_data = TrackData(self.title,
                                   None,
                                   self.description,
                                   [self.user.username],
                                   self.user.username,
                                   self.album_name if self.album_name is not "" else self.title,
                                   int(self.display_date.split("-")[0]),
                                   self.track_index if self.track_index > 0 else 1,
                                   self.genre,
                                   False,
                                   self.artwork_url)
            for audio_stream in data["media"]["transcodings"]:
                self.streams.append(SoundCloudStream(audio_stream, client_id, track_data))

    def generate_album_info(self, parent):
        track_index = 0
        found_track: bool = False
        album = parent.albums(self.id, "full", 1, 0)
        if (album is not False):
            album = album[0]
            self.album_name = album.title
            for album_track in album.tracks:
                if (not found_track):
                    track_index += 1
                    if (album_track.id == self.id):
                        found_track = True
                        self.track_index = track_index

    def __str__(self) -> str:
        string_out = 'SoundCloudTrack(comment_count: {}, full_duration: {}, downloadable: {}, created_at: "{}", ' \
                     'description: "{}", title: "{}", duration: {}, has_downloads_left: {}, artwork_url: "{}", ' \
                     'public: {}, streamable: {}, genre: "{}", id: {}, reposts_count: {}, state: "{}", ' \
                     'label_name: "{}", last_modified: "{}", commentable: {}, policy: "{}", purchase_url: "{}", ' \
                     'sharing: "{}", uri: "{}", download_count: {}, likes_count: {}, urn: "{}", license: "{}", ' \
                     'purchase_title: "{}", display_date: "{}", user_id: {}, monetization_model: "{}", ' \
                     'waveform_url: "{}", permalink: "{}",' \
                     'permalink_url: "{}", user: {})'.format(self.comment_count,
                                                             self.full_duration,
                                                             self.downloadable,
                                                             self.created_at,
                                                             self.description.replace("\n", "\\n"),
                                                             self.title,
                                                             self.duration,
                                                             self.has_downloads_left,
                                                             self.artwork_url,
                                                             self.public,
                                                             self.streamable,
                                                             self.genre,
                                                             self.id,
                                                             self.reposts_count,
                                                             self.state,
                                                             self.label_name,
                                                             self.last_modified,
                                                             self.commentable,
                                                             self.policy,
                                                             self.purchase_url,
                                                             self.sharing,
                                                             self.uri,
                                                             self.download_count,
                                                             self.likes_count,
                                                             self.urn,
                                                             self.license,
                                                             self.purchase_title,
                                                             self.display_date,
                                                             self.user_id,
                                                             self.monetization_model,
                                                             self.waveform_url,
                                                             self.permalink,
                                                             self.permalink_url,
                                                             self.user)
        return string_out

    def __repr__(self) -> str:
        return self.__str__()
