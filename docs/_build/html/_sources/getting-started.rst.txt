===============
Getting Started
===============

Installation
============
To install PySoundCloud use pip

.. code-block:: shell

    $ pip install pysoundcloud

The wheel file can also be downloaded from `here <https://github.com/AnthonyWritesBadCode/PySoundCloud/raw/master/dist/PySoundCloud-2020.6.1-py3-none-any.whl>`_ on GitHub and the source code from
the `GitHub repo <https://github.com/AnthonyWritesBadCode/PySoundCloud>`_.

Basic Usage
===========
To start using PySoundCloud simply import the Client and insert your client ID from the SoundCloud API.

.. code-block:: python

    from pysoudcloud import Client
    client = Client("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


.. _client_id:

Client ID
==========
SoundCloud has stopped providing keys to be used with their API, however you can still obtain one in three easy steps:

Step One
********
Open the SoundCloud website and open the developer tools, or equivalent in other browsers (Chrome: F12 or Ctrl+Shift+I,
Edge: F12) and head over to the *network* tab. You should have a lot of requests showing up. If you don't, then just refresh the page.

.. image:: images/step_1.png

Step Two
********
In the networking tab, at the top, search for :code:`client_id` and select any of the results that contains it.

.. image:: images/step_2.png

Step Three
**********
In your results, there should be a request like this:

.. code-block:: text

    https://api-v2.soundcloud.com/me/play-history/tracks?client_id=PgKFRG98vbasF0IWR0AuZ09A4Tg•••••limit=25&offset=0&linked_partitioning=1&app_version=1591082147&app_locale=en

So from this, my client ID is :code:`PgKFRG98vbasF0IWR0AuZ09A4Tg•••••`, which can be used in the code like this:

.. code-block:: python

    client = Client("PgKFRG98vbasF0IWR0AuZ09A4Tg•••••")

.. image:: images/step_3_censored.png