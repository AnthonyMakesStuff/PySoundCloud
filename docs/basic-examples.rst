==============
Basic Examples
==============

For all of these examples, it's assumed that you've imported PySoundCloud and assigned the client:

.. code-block:: python

    from pysoundcloud import Client
    client = Client("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

Search For a Track & Download It
================================
This example shows how to search for a song and download it. In this case, the song is
`XYconstant - Her Eyes (EKAE Remix) <https://soundcloud.com/ekae/hereyesremix>`_.

.. code-block:: python

    results = client.search("XYconstant her eyes ekae remix")
    results[0].streams[1].download()
    # File created: downloads/EKAE - XYconstant - Her Eyes (EKAE Remix).mp3


.. warning::
    Unfortunately, not all tracks can be downloaded. I'm not really sure why this is the case, but my guess is that it's
    a form of DRM.


Download All Tracks In a Playlist
=================================
This example shows how to download all songs in a playlist. For this example, I'm going to download all the tracks in my
playlist `Pavorite Flaylist <https://soundcloud.com/anthonyprovenza/sets/pavorite-flaylist>`_. In my playlist all the
tracks will download without any issues, however, it's better to be safe and adding the exception catching is quick and
easy.

.. code-block:: python

    playlist = client.playlist(playlist_url="https://soundcloud.com/anthonyprovenza/sets/pavorite-flaylist")

    for track in playlist.tracks:
        track = client.track(track.id)
        print(f"Downloading {track.title} by {track.user.username}")
        try:
            track.streams[1].download()
        except IndexError as e:
            print(e)


.. note::
    When getting all the tracks in a playlist, the API only returns full information for the first few tracks. As a
    result, it's safest to also call :code:`track = client.track(track.id)` to get all the data for the track.


Get The ID of a Playlist
========================
This example is useless, however, I wanted to test the time difference between using a playlist's URl and its ID.
In theory the playlist ID will always be faster, as it's only one request and requires less processing. In this case,
the difference isn't too dramatic but is still visible, so it's always better to use the playlist's ID when possible.

**By URL**

.. code-block:: python

    import time

    start_time = time.time()
    playlist = client.playlist(playlist_url="https://soundcloud.com/anthonyprovenza/sets/pavorite-flaylist")
    print(playlist.id)
    end_time = time.time()
    print(end_time - start_time)

**By ID**

.. code-block:: python

    import time

    start_time = time.time()
    playlist = client.playlist(284506067)
    print(playlist.id)
    end_time = time.time()
    print(end_time - start_time)

**Timings**

+------+--------------+-------------+
| Time | Playlist URL | Playlist ID |
+======+==============+=============+
| 1    | 10.15295291  | 10.53369117 |
+------+--------------+-------------+
| 2    | 10.28002214  | 9.883991957 |
+------+--------------+-------------+
| 3    | 11.02119231  | 9.912426233 |
+------+--------------+-------------+
| 4    | 10.84462953  | 9.993349314 |
+------+--------------+-------------+
| 5    | 10.59322929  | 11.44314289 |
+------+--------------+-------------+
| Avg. | 10.57840524  | 10.35332031 |
+------+--------------+-------------+

.. note::
    The :code:`time.time()` generates a number to 15 decimal places. Excel rounded the numbers to 8 decimal places, but
    (I think) it calculated the average based on the original numbers then rounded them.
