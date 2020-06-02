from contextlib import suppress
from typing import Union, List

from requests.models import Response

from pysoundcloud.soundclouddata import SoundCloudData
from pysoundcloud.soundclouduser import SoundCloudUser
from pysoundcloud.soundcloudtrack import SoundCloudTrack
from pysoundcloud.soundcloudplaylist import SoundCloudPlaylist


class SoundCloudSearchResults:
    response_json: dict = dict()
    response_content: str = ""
    url: str = ""
    total_results: int = 0
    next_href: str = ""
    results: List[Union[SoundCloudUser, SoundCloudTrack, SoundCloudPlaylist]] = list()

    """
    :var response_json: The json dict from the response
    :var response_content: The str content from the response
    :var url: The url for the search?
    :var total_results: The total number of results for the search query
    :var next_href: The link to the next page of results
    :var results: All the results for the search query
    """

    def __init__(self, response: Response, client_id: str = None, parent: "pysoundcloud.client.Client" = None) -> None:
        """
        :param response: The requests response
        :param client_id: The ID of the client
        :param parent:
        """
        self.response_json = response.json()
        self.response_content = response.content.decode("utf-8")
        self.url = response.url
        self.total_results = self.response_json["total_results"]
        with suppress(KeyError):
            self.next_href = self.response_json["next_href"]

        for i in range(len(self.response_json["collection"])):
            kind = self.response_json["collection"][i]["kind"]
            if (kind == "user"):
                self.results.append(SoundCloudUser(self.response_json["collection"][i],
                                                   client_id))
            elif (kind == "track"):
                self.results.append(SoundCloudTrack(self.response_json["collection"][i],
                                                    client_id, parent=parent))
            elif (kind == "playlist"):
                self.results.append(SoundCloudPlaylist(self.response_json["collection"][i],
                                                       client_id))
            else:
                print(self.response_json["collection"][i]["kind"])

    def __getitem__(self, item):
        return self.results[item]
