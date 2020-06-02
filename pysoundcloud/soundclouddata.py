from requests.models import Response


class SoundCloudData:
    response_json: dict = ""
    response_content: str = ""

    """
    :var response_json: The json from the requests response
    :var response_content: The decoded content of the response
    """

    def __init__(self, response: Response) -> None:
        self.response_json = response.json()
        self.response_content = response.content.decode("utf-8")

    def __str__(self):
        return self.response_content

    def __repr__(self):
        return "SoundCloudData({})".format(self.response_content)
