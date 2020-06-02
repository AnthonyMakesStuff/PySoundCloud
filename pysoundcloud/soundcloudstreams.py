from typing import List

from pysoundcloud.soundcloudstream import SoundCloudStream


class SoundCloudStreams:
    streams: List[SoundCloudStream] = None

    """
    :var streams: Contains a list of all the streams
    """

    def __init__(self):
        self.streams = list()

    def append(self, item):
        self.streams.append(item)

    def all(self) -> List[SoundCloudStream]:
        return self.streams

    def __getitem__(self, item):
        return self.streams[item]

    def first(self) -> SoundCloudStream:
        """
        Get the first stream in the list

        :return: The first SoundCloudStream
        """
        return self.streams[0]

    def last(self) -> SoundCloudStream:
        """
        Get the last stream in the list

        :return: The last SoundCloudStream
        """
        return self.streams[-1]

    def filter(self,
               preset: str = None,
               snipped: bool = False,
               format_protocol_progressive: bool = None,
               format_protocol_hls: bool = None,
               format_mime_type_mpeg: bool = None,
               format_mime_type_ogg: bool = None,
               format_codecs_opus: bool = None) -> list:
        """
        Filter the streams by certain parameters

        .. note::
            Not all of the parameters are currently implemented

        :param preset: Preset string
        :param snipped: Should the stream be snipped?
        :param format_protocol_progressive: Should the stream protocol be progressive?
        :param format_protocol_hls: Should the stream protocol be hls?
        :param format_mime_type_mpeg: Should the stream mime type be mpeg?
        :param format_mime_type_ogg: Should the stream mime type be ogg?
        :param format_codecs_opus: Should the codec be opus?
        :return: A list with the streams that match the filters
        """
        # Todo: Add all the filters
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
