from typing import List


class TrackData:
    track_title: str = ""
    track_subtitle: str = ""
    track_comments: str = ""
    track_artists: List[str] = list()
    album_artist: str = ""
    album_title: str = ""
    album_year: int = 0
    track_number: int = 0
    genre: str = ""
    part_of_compilation: bool = False
    album_artwork_url: str = ""

    def __init__(self,
                 track_title: str = None,
                 track_subtitle: str = None,
                 track_comments: str = None,
                 track_artists: List[str] = None,
                 album_artist: str = None,
                 album_title: str = None,
                 album_year: int = None,
                 track_number: int = None,
                 genre: str = None,
                 part_of_compilation: bool = False,
                 album_artwork_url: str = None):
        self.track_title = track_title
        self.track_subtitle = track_subtitle
        self.track_comments = track_comments
        self.track_artists = track_artists
        self.album_artist = album_artist
        self.album_title = album_title
        self.album_year = album_year
        self.track_number = track_number
        self.genre = genre
        self.part_of_compilation = part_of_compilation
        self.album_artwork_url = album_artwork_url
