from typing import List

from pysoundcloud.soundcloudstream import SoundCloudStream


class SoundCloudStreams:
    streams: List[SoundCloudStream] = None

    def __init__(self):
        self.streams = list()

    def append(self, item):
        self.streams.append(item)

    def all(self) -> List[SoundCloudStream]:
        return self.streams

    def __getitem__(self, item):
        return self.streams[item]

    def first(self) -> SoundCloudStream:
        return self.streams[0]

    def last(self) -> SoundCloudStream:
        return self.streams[-1]

    def filter(self,
               preset: str = None,
               snipped: bool = False,
               format_protocol_progressive: bool = None,
               format_protocol_hls: bool = None,
               format_mime_type_mpeg: bool = None,
               format_mime_type_ogg: bool = None,
               format_codecs_opus: bool = None) -> list:
        # Todo: Add the filters
        list_out: List[SoundCloudStream] = self.streams
        temp_list: List[SoundCloudStream] = []
        if (preset is not None):
            for item in list_out:
                if (item.preset == preset):
                    temp_list.append(item)
            list_out = temp_list
            temp_list = []
        if (snipped is not None):
            for item in list_out:
                if (item.snipped == snipped):
                    temp_list.append(item)
            list_out = temp_list
            temp_list = []
        if (format_protocol_progressive is not None):
            for item in list_out:
                if (item.format.protocol == "progressive"):
                    temp_list.append(item)
            list_out = temp_list

        if (format_mime_type_mpeg is not None):
            for item in list_out:
                if (item.format.mime_type == "audio/mpeg"):
                    temp_list.append(item)
            list_out = temp_list

        return list_out

    def __str__(self) -> str:
        return "SoundCloudStreams({})".format(self.streams)

    def __repr__(self) -> str:
        return self.__str__()
