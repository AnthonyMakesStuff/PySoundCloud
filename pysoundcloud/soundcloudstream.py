import os
import re
import requests
import shutil
import urllib3

from mutagen.id3 import ID3

# noinspection PyProtectedMember
from mutagen.id3._frames import TIT3
# noinspection PyProtectedMember
from mutagen.id3._frames import APIC
# noinspection PyProtectedMember
from mutagen.id3._frames import TRCK

# noinspection PyProtectedMember
from mutagen.id3._frames import TIT2
# noinspection PyProtectedMember
from mutagen.id3._frames import TALB
# noinspection PyProtectedMember
from mutagen.id3._frames import TPE1
# noinspection PyProtectedMember
from mutagen.id3._frames import TPE2
# noinspection PyProtectedMember
from mutagen.id3._frames import COMM
# noinspection PyProtectedMember
from mutagen.id3._frames import TCON
# noinspection PyProtectedMember
from mutagen.id3._frames import TDRC

from pysoundcloud.trackdata import TrackData


class StreamFormat:
    protocol: str = ""
    mime_type: str = ""

    """
    :var protocol: The protocol of the stream
    :var mime_type: The mime type of the stream
    """

    def __init__(self,
                 protocol: str,
                 mime_type: str):
        self.protocol = protocol
        self.mime_type = mime_type

    def __str__(self) -> str:
        return 'StreamFormat(protocol: "{}", mime_type: "{}")'.format(self.protocol,
                                                                      self.mime_type)

    def __repr__(self) -> str:
        return self.__str__()


class SoundCloudStream:
    url: str = ""
    preset: str = ""
    duration: int = 0
    snipped: bool = False
    format: StreamFormat = None
    quality: str = ""
    client_id: str = None
    track_data: TrackData = None

    """
    :var url: The url of the stream
    :var preset:
    :var duration: The duration of the stream (in milleseconds?)
    :var snipped:
    :var format: The format of the stream
    :var quality:
    :var client_id: The ID of the client
    :var track_data: The data of the track
    """

    def __init__(self,
                 data: dict,
                 client_id: str = None,
                 track_data: TrackData = None) -> None:
        """
        :param data: The json dict from the response
        :param client_id: The ID of the client
        :param track_data: The data of the track
        """
        self.url = data["url"]
        self.track_data = track_data
        if (client_id is not None):
            self.client_id = client_id
            self.url += "?client_id=" + client_id
        self.preset = data["preset"]
        self.duration = data["duration"]
        self.snipped = data["snipped"]
        self.format = StreamFormat(data["format"]["protocol"],
                                   data["format"]["mime_type"])
        self.quality = data["quality"]

    def download(self,
                 location: str = "downloads/",
                 file_name: str = None,
                 use_better_file_name: bool = True,
                 use_album_data: bool = True,
                 artwork_url: str = None,
                 artwork_crop_to_square: bool = True) -> None:
        """
        Download the stream

        .. note::
            When downloading a stream, it also attempts to download metadata and album artwork for it. The artists is
            the username user who uploaded the track, the title is the track title on SoundCloud and the artwork is
            whatever is provided with the track. It also does a quick check to see if the track appears in any albums.
            If it does, then it gets the first album and then gets album info and artwork from there instead.

        :param location: The location to download the stream to
        :param file_name: The name of the file
        :param use_better_file_name: If no file name specified, create one using the username and track title?
        :param use_album_data: Use the data of the first album that the track is in
        :param artwork_url: The url of the artwork to use
        :param artwork_crop_to_square: Should the artwork be cropped to a square? (Not currently used)
        :return: None
        """
        if (self.client_id is not None):
            response = requests.get(self.url, stream=True)
            if (response.status_code != 200):
                print(f"Error: Could not download the file. (Status code {response.status_code})")
                return
            download_url = response.json()["url"]
            if (file_name is None):
                file_name = re.search(r"[a-zA-Z0-9\-]*\.[0-9]+\.(mp3|opus)",
                                      download_url).group()
                if (use_better_file_name and
                        self.track_data is not None and
                        self.track_data.track_artists is not None and
                        self.track_data.track_title is not None):
                    extension = file_name.split(".")[-1]
                    file_name = "{} - {}.{}".format(self.track_data.track_artists[0],
                                                    self.track_data.track_title,
                                                    extension)
            file_name = SoundCloudStream.sanitize_file_name(file_name)
            if (not os.path.exists(location)):
                os.mkdir(location)
            output_location = os.path.join(location, file_name)
            http = urllib3.PoolManager()
            with http.request('GET', download_url, preload_content=False) as r, open(output_location, 'wb') as out_file:
                shutil.copyfileobj(r, out_file)
            try:
                tags = ID3(output_location)
            except Exception:
                tags = ID3()

            if (self.track_data is not None):
                # tags["TIT1"] = TIT1(encoding=3, text="Group description")
                if (self.track_data.track_title is not None):
                    tags["TIT2"] = TIT2(encoding=3, text=self.track_data.track_title)
                if (self.track_data.track_subtitle is not None):
                    tags["TIT3"] = TIT3(encoding=3, text=self.track_data)
                if (self.track_data.track_comments is not None):
                    tags["COMM"] = COMM(encoding=3, lang=u"eng", desc=self.track_data.track_comments)
                if (self.track_data.track_artists is not []):
                    tags["TPE1"] = TPE1(encoding=3, text=self.track_data.track_artists[0])
                if (self.track_data.album_artist is not None):
                    tags["TPE2"] = TPE2(encoding=3, text=self.track_data.album_artist)
                if (self.track_data.album_title is not None):
                    tags["TALB"] = TALB(encoding=3, text=self.track_data.album_title)
                if (self.track_data.album_year is not None):
                    tags["TDRC"] = TDRC(encoding=3, text=str(self.track_data.album_year))
                if (self.track_data.track_number is not None):
                    tags["TRCK"] = TRCK(encoding=3, text="{}/0".format(self.track_data.track_number))
                if (self.track_data.genre is not None):
                    tags["TCON"] = TCON(encoding=3, text=self.track_data.genre)
                if (self.track_data.album_artwork_url is not None):
                    url = self.track_data.album_artwork_url.replace("large", "t500x500")
                    with http.request("GET", url, preload_content=False) as r,\
                            open(output_location + ".jpg", "wb") as out_file:
                        shutil.copyfileobj(r, out_file)
                    with open(output_location + ".jpg", "rb") as album_art:
                        tags["APIC"] = APIC(encoding=3, mime="image/jpeg", type=3, desc=u"cover",
                                            data=album_art.read())
                    os.remove(output_location + ".jpg")

            tags.save(output_location)
        else:
            print("Error: No client ID provided")

    @staticmethod
    def sanitize_file_name(file_name: str) -> str:
        """
        Sanitizes the file name as to not create any errors on Windows.
        Hopfully works on other OSes but should be easy to add on to, if not

        :param file_name: The file name to sanitize
        :return: The sanitized file name
        """
        file_name = file_name.replace("\\", "")
        file_name = file_name.replace("/", "")
        file_name = file_name.replace(":", "")
        file_name = file_name.replace("*", "")
        file_name = file_name.replace("?", "")
        file_name = file_name.replace("\"", "")
        file_name = file_name.replace("<", "")
        file_name = file_name.replace(">", "")
        file_name = file_name.replace("|", "")
        return file_name

    def __str__(self) -> str:
        string_out = 'SoundCloudStream(url: "{}", preset: "{}", duration: {}, snipped: {}, format: {}, ' \
                     'quality: "{}")'.format(self.url,
                                             self.preset,
                                             self.duration,
                                             self.snipped,
                                             self.format,
                                             self.format)
        return string_out

    def __repr__(self) -> str:
        return self.__str__()
