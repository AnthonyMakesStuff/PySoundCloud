from requests.models import Response
from typing import List

from pysoundcloud.soundcloudtrack import SoundCloudTrack


class SoundCloudLikedTrack:
    created_at: str = ""
    track: SoundCloudTrack = None

    def __init__(self,
                 created_at: str,
                 track: SoundCloudTrack):
        self.created_at = created_at
        self.track = track

    def __str__(self) -> str:
        return 'SoundCloudLikedTrack(created_at: "{}", track: {})'.format(self.created_at,
                                                                          self.track)

    def __repr__(self) -> str:
        return self.__str__()


class SoundCloudLikedTracks:
    response_json: dict = dict()
    response_content: str = ""
    url: str = ""
    next_href: str = ""
    liked_tracks: List[SoundCloudLikedTrack] = list()
    index: int = 0

    def __init__(self, response: Response, client_id: str = None) -> None:
        self.response_json = response.json()
        self.response_content = response.content.decode("utf-8")
        self.url = response.url
        self.next_href = self.response_json["next_href"]
        for i in range(len(self.response_json["collection"])):
            data = self.response_json["collection"][i]
            self.liked_tracks.append(SoundCloudLikedTrack(data["created_at"],
                                                          SoundCloudTrack(data["track"],
                                                                          client_id,
                                                                          playlist_track_index=i+1)))

    def __iter__(self):
        return self

    def __next__(self) -> SoundCloudLikedTrack:
        try:
            value = self.liked_tracks[self.index]
            self.index += 1
            return value
        except IndexError:
            raise StopIteration

    def __str__(self) -> str:
        string_out = "SoundCloudLikedTracks("
        for track in self.liked_tracks:
            string_out += str(track) + ", \n"
        string_out += ")"
        return string_out
