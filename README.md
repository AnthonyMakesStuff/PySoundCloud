# PySoundCloud
PySoundCloud is a Python wrapper for the SoundCloud API.

## Installation
To install the latest version use
```
pip install pysoundcloud
```

## Basic Usage
To use PySoundCloud just import the client. This handles all of the interactions with the API
```python
from pysoundcloud import Client
# Replace this with your client ID
client = Client("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
```

From there you can use all of the functions of the client. The following example searches for the track
`her eyes ekae remix` and then prints the artist of the track and the title
```python
results = client.search("her eyes ekae remix")
track_title = results[0].title
track_artist = results[0].user.username
print(f"{track_artist} - {track_title}")
```
View the [basic examples](https://pysoundcloud.readthedocs.io/en/latest/basic-examples.html) on Read the Docs for more

## Useful Links
- [PyPI Project](https://pypi.org/project/PySoundCloud/)
- [Documentation](https://pysoundcloud.readthedocs.io/) on Read the Docs
- [GitHub](https://github.com/AnthonyWritesBadCode/PySoundCloud) (you're already here)
