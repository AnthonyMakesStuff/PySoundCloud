from contextlib import suppress


class SoundCloudUser:
    avatar_url: str = ""
    city: str = ""
    comments_count: int = 0
    country_code: str = ""
    created_at: str = ""
    description: str = ""
    followers_count: int = 0
    followings_count: int = 0
    first_name: str = ""
    last_name: str = ""
    full_name: str = ""
    groups_count: int = 0
    id: int = 0
    last_modified: str = ""
    likes_count: int = 0
    playlist_likes_count: int = 0
    permalink: str = ""
    playlist_count: int = 0
    reposts_count: int = 0
    track_count: int = 0
    uri: str = ""
    urn: str = ""
    username: str = ""
    verified: bool = False

    """
    :var avatar_url: [SC] URL to a JPEG image
    :var city: [SC] City
    :var comments_count: The number of public comments
    :var country_code: The country code of the user
    :var created_at: Timestamp the user signed up?
    :var description: [SC] Description
    :var followers_count: [SC] Number of followers
    :var followings_count: [SC] Number of followed users
    :var first_name: The user's first name
    :var last_name: The user's last name
    :var full_name: [SC] First and last name
    :var groups_count: Number of groups the user is in
    :var id: The integer ID of the user
    :var last_modified: Timestamp the profile was last edited?
    :var likes_count: Number of likes
    :var playlist_likes_count: Number of playlists liked
    :var permalink: [SC] Permalink of the resource
    :var playlist_count: [SC] Number of public playlists
    :var reposts_count: Number of reposts
    :var track_count: [SC] Number of public tracks
    :var uri: [SC] API resource URL
    :var urn: (No idea)
    :var username: [SC] Username
    :var verified: Is the user verified
    """

    def __init__(self, data: dict, client_id: str = None):
        """
        :param data: The json dict from the response
        :param client_id: The ID of the client
        """
        self.avatar_url = data["avatar_url"]
        self.city = data["city"]
        self.country_code = data["country_code"]
        # Todo: add subscriptions
        with suppress(KeyError):
            self.comments_count = data["comments_count"]
            self.created_at = data["created_at"]
            self.description = data["description"] if data["description"] is not None else ""
            self.followers_count = data["followers_count"]
            self.followings_count = data["followings_count"]
            self.groups_count = data["groups_count"]
            self.likes_count = data["likes_count"]
            self.playlist_likes_count = data["playlist_likes_count"]
            self.playlist_count = data["playlist_count"]
            self.reposts_count = data["reposts_count"]
            self.track_count = data["track_count"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.full_name = data["full_name"]
        self.id = data["id"]
        self.last_modified = data["last_modified"]
        self.permalink = data["permalink"]
        self.uri = data["uri"]
        self.urn = data["urn"]
        self.username = data["username"]
        self.verified = data["verified"]

    def __str__(self) -> str:
        string_out = 'SoundCloudUser(avatar_url: "{}", city: "{}", comments_count: {}, country_code: "{}", ' \
                     'created_at: "{}", description: "{}", followers_count: {}, followings_count: {}, ' \
                     'first_name: "{}", last_name: "{}", full_name: "{}", groups_count: {}, id: {}, ' \
                     'last_modified: "{}", likes_count: {}, playlist_likes_count: {}, permalink: "{}", ' \
                     'playlist_count: {}, reposts_count: {}, track_count: {}, uri: "{}", urn: "{}", username: "{}", ' \
                     'verified: {})'.format(self.avatar_url,
                                            self.city,
                                            self.comments_count,
                                            self.country_code,
                                            self.created_at,
                                            self.description.replace("\n", "\\n"),
                                            self.followers_count,
                                            self.followings_count,
                                            self.first_name,
                                            self.last_name,
                                            self.full_name,
                                            self.groups_count,
                                            self.id,
                                            self.last_modified,
                                            self.likes_count,
                                            self.playlist_likes_count,
                                            self.permalink,
                                            self.playlist_count,
                                            self.reposts_count,
                                            self.track_count,
                                            self.uri,
                                            self.urn,
                                            self.username,
                                            self.verified)
        return string_out

    def __repr__(self) -> str:
        return self.__str__()

